from functools import partial
from typing import Callable, Dict, Optional, Union

import numpy as np
import torch
from torch import nn
import torch.nn.functional as F
from torch.optim.lr_scheduler import ReduceLROnPlateau

from collie_recs.model.base import BasePipeline, INTERACTIONS_LIKE_INPUT, ScaledEmbedding
from collie_recs.utils import get_init_arguments, trunc_normal


class NeuralCollaborativeFiltering(BasePipeline):
    """
    Training pipeline for a neural matrix factorization model.

    ``NeuralCollaborativeFiltering`` models combine a collaborative filtering and multilayer
    perceptron network in a single, unified model. The model consists of two sections: the first
    is a simple matrix factorization that calculates a score by multiplying together user and item
    embeddings (lookups through an embedding table); the second is a MLP network that feeds
    embeddings from a second set of embedding tables (one for user, one for item). Both output
    vectors are combined and sent through a final MLP layer before returning a single recommendation
    score.

    The implementation here is meant to mimic its original implementation as specified here:
    https://arxiv.org/pdf/1708.05031.pdf [1]_

    All ``NeuralCollaborativeFiltering`` instances are subclasses of the ``LightningModule`` class
    provided by PyTorch Lightning. This means to train a model, you will need a
    ``collie_recs.model.CollieTrainer`` object, but the model can be saved and loaded without this
    ``Trainer`` instance. Example usage may look like:

    .. code-block:: python

        from collie_recs.model import CollieTrainer, NeuralCollaborativeFiltering


        model = NeuralCollaborativeFiltering(train=train)
        trainer = CollieTrainer(model)
        trainer.fit(model)
        model.freeze()

        # do evaluation as normal with ``model``

        model.save_model(filename='model.pth')
        new_model = NeuralCollaborativeFiltering(load_model_path='model.pth')

        # do evaluation as normal with ``new_model``

    Parameters
    ----------
    train: ``collie_recs.interactions`` object
        Data loader for training data. If an ``Interactions`` object is supplied, an
        ``InteractionsDataLoader`` will automatically be instantiated with ``shuffle=True``. Note
        that when the model class is saved, datasets will NOT be saved as well
    val: ``collie_recs.interactions`` object
        Data loader for validation data. If an ``Interactions`` object is supplied, an
        ``InteractionsDataLoader`` will automatically be instantiated with ``shuffle=False``. Note
        that when the model class is saved, datasets will NOT be saved as well
    embedding_dim: int
        Number of latent factors to use for the matrix factorization embedding table. For the MLP
        embedding table, the dimensionality will be calculated with the formula
        ``embedding_dim * (2 ** (num_layers - 1))``
    num_layers: int
        Number of MLP layers to apply. Each MLP layer will have its input dimension calculated with
        the formula ``embedding_dim * (2 ** (``num_layers`` - ``current_layer_number``))``
    final_layer: str or function
        Final layer activation function. Available string options include:

        * 'sigmoid'

        * 'relu'

        * 'leaky_relu'

    dropout_p: float
        Probability of dropout on the MLP layers
    lr: float
        Model learning rate
    lr_scheduler_func: torch.optim.lr_scheduler
        Learning rate scheduler to use during fitting
    weight_decay: float
        Weight decay passed to the optimizer, if optimizer permits
    optimizer: torch.optim or str
        If a string, one of the following supported optimizers:

        * ``'sgd'`` (for ``torch.optim.SGD``)

        * ``'adam'`` (for ``torch.optim.Adam``)

    loss: function or str
        If a string, one of the following implemented losses:

        * ``'bpr'`` / ``'adaptive_bpr'``

        * ``'hinge'`` / ``'adaptive_hinge'``

        * ``'warp'``

        If ``train.num_negative_samples > 1``, the adaptive loss version will automatically be used
    metadata_for_loss: dict
        Keys should be strings identifying each metadata type that match keys in
        ``metadata_weights``. Values should be a ``torch.tensor`` of shape (num_items x 1). Each
        tensor should contain categorical metadata information about items (e.g. a number
        representing the genre of the item)
    metadata_for_loss_weights: dict
        Keys should be strings identifying each metadata type that match keys in ``metadata``.
        Values should be the amount of weight to place on a match of that type of metadata, with
        the sum of all values ``<= 1``.
        e.g. If ``metadata_for_loss_weights = {'genre': .3, 'director': .2}``, then an item is:

        * a 100% match if it's the same item,

        * a 50% match if it's a different item with the same genre and same director,

        * a 30% match if it's a different item with the same genre and different director,

        * a 20% match if it's a different item with a different genre and same director,

        * a 0% match if it's a different item with a different genre and different director,
          which is equivalent to the loss without any partial credit
    load_model_path: str or Path
        To load a previously-saved model, pass in path to output of ``model.save_model()`` method.
        If ``None``, will initialize model as normal
    map_location: str or torch.device
        If ``load_model_path`` is provided, device specifying how to remap storage locations when
        ``torch.load``-ing the state dictionary

    References
    -------------
    .. [1] Xiangnan et al. "Neural Collaborative Filtering." Neural Collaborative Filtering |
        Proceedings of the 26th International Conference on World Wide Web, 1 Apr. 2017,
        dl.acm.org/doi/10.1145/3038912.3052569.

    """
    def __init__(self,
                 train: INTERACTIONS_LIKE_INPUT = None,
                 val: INTERACTIONS_LIKE_INPUT = None,
                 embedding_dim: int = 8,
                 num_layers: int = 3,
                 final_layer: Optional[Union[str, Callable]] = None,
                 dropout_p: float = 0.0,
                 lr: float = 1e-3,
                 lr_scheduler_func: Optional[Callable] = partial(ReduceLROnPlateau,
                                                                 patience=1,
                                                                 verbose=True),
                 weight_decay: float = 0.0,
                 optimizer: Union[str, Callable] = 'adam',
                 loss: Union[str, Callable] = 'hinge',
                 metadata_for_loss: Optional[Dict[str, torch.tensor]] = None,
                 metadata_for_loss_weights: Optional[Dict[str, float]] = None,
                 # y_range: Optional[Tuple[float, float]] = None,
                 load_model_path: Optional[str] = None,
                 map_location: Optional[str] = None):
        super().__init__(**get_init_arguments())

    def _setup_model(self, **kwargs) -> None:
        """
        Method for building model internals that rely on the data passed in.

        This method will be called after ``prepare_data``.

        """
        self.user_embeddings_cf = ScaledEmbedding(num_embeddings=self.hparams.num_users,
                                                  embedding_dim=self.hparams.embedding_dim)
        self.item_embeddings_cf = ScaledEmbedding(num_embeddings=self.hparams.num_items,
                                                  embedding_dim=self.hparams.embedding_dim)

        mlp_embedding_dim = self.hparams.embedding_dim * (2 ** (self.hparams.num_layers - 1))
        self.user_embeddings_mlp = ScaledEmbedding(
            num_embeddings=self.hparams.num_users,
            embedding_dim=mlp_embedding_dim,
        )
        self.item_embeddings_mlp = ScaledEmbedding(
            num_embeddings=self.hparams.num_items,
            embedding_dim=mlp_embedding_dim,
        )

        mlp_modules = []
        for i in range(self.hparams.num_layers):
            input_size = self.hparams.embedding_dim * (2 ** (self.hparams.num_layers - i))
            mlp_modules.append(nn.Dropout(p=self.hparams.dropout_p))
            mlp_modules.append(nn.Linear(input_size, input_size//2))
            mlp_modules.append(nn.ReLU())
        self.mlp_layers = nn.Sequential(*mlp_modules)

        self.predict_layer = nn.Linear(self.hparams.embedding_dim * 2, 1)

        for m in self.mlp_layers:
            if isinstance(m, nn.Linear):
                # initialization taken from the official repo:
                # https://github.com/hexiangnan/neural_collaborative_filtering/blob/master/NeuMF.py#L63  # noqa: E501
                trunc_normal(m.weight.data, std=0.01)

        nn.init.kaiming_uniform_(self.predict_layer.weight, nonlinearity='relu')

        for m in self.modules():
            if isinstance(m, nn.Linear) and m.bias is not None:
                m.bias.data.zero_()

    def forward(self, users: torch.tensor, items: torch.tensor) -> torch.tensor:
        """
        Forward pass through the model.

        Parameters
        ----------
        users: tensor, 1-d
            Array of user indices
        items: tensor, 1-d
            Array of item indices

        Returns
        -------
        preds: tensor, 1-d
            Predicted ratings or rankings

        """
        user_embedding_cf = self.user_embeddings_cf(users)
        item_embedding_cf = self.item_embeddings_cf(items)
        output_cf = user_embedding_cf * item_embedding_cf

        user_embedding_mlp = self.user_embeddings_mlp(users)
        item_embedding_mlp = self.item_embeddings_mlp(items)
        interaction = torch.cat((user_embedding_mlp, item_embedding_mlp), -1)
        output_mlp = self.mlp_layers(interaction)

        concat = torch.cat((output_cf, output_mlp), -1)

        prediction = self.predict_layer(concat)

        if callable(self.hparams.final_layer):
            prediction = self.hparams.final_layer(prediction)
        elif self.hparams.final_layer == 'sigmoid':
            prediction = torch.sigmoid(prediction)
        elif self.hparams.final_layer == 'relu':
            prediction = F.relu(prediction)
        elif self.hparams.final_layer == 'leaky_relu':
            prediction = F.leaky_relu(prediction)
        elif self.hparams.final_layer is not None:
            raise ValueError(f'{self.hparams.final_layer} not valid final layer value!')

        return prediction.view(-1)

    def _get_item_embeddings(self) -> np.array:
        """Get item embeddings, which are the concatenated CF and MLP item embeddings."""
        items = torch.arange(self.hparams.num_items, device=self.device)

        return np.concatenate((
            self.item_embeddings_cf(items).detach().cpu(),
            self.item_embeddings_mlp(items).detach().cpu()
        ), axis=1)
