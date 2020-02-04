# Copyright © 2017-2020 Alexander L. Hayes

"""
Markov Logic Networks
"""

from .base import BaseBoostedRelationalModel


class BoostedMLN(BaseBoostedRelationalModel):
    """Markov Logic Networks Estimator

    Wrappers around BoostSRL for learning and inference with Boosted
    Markov Logic Networks written with a scikit-learn-style interface
    derived from :class:`srlearn.base.BaseEstimator`

    Examples
    --------

    >>> from srlearn.mln import BoostedMLN
    >>> from srlearn.background import Background
    >>> from srlearn import example_data
    """

    def __init__(
        self,
        background=None,
        target="None",
        n_estimators=10,
        node_size=2,
        max_tree_depth=3,
    ):
        """Initialize a BoostedMLN

        Parameters
        ----------
        background : :class:`srlearn.background.Background` (default: None)
            Background knowledge with respect to the database
        target : str (default: "None")
            Target predicate to learn
        n_estimators : int, optional (default: 10)
            Number of trees to fit
        node_size : int, optional (default: 2)
            Maximum number of literals in each node.
        max_tree_depth : int, optional (default: 3)
            Maximum number of nodes from root to leaf (height) in the tree.
        """

        super().__init__(
            background=background,
            target=target,
            n_estimators=n_estimators,
            node_size=node_size,
            max_tree_depth=max_tree_depth,
        )

        def fit(self, database):
            pass

        def _run_inference(self, database) -> None:
            pass

        def predict(self, database):
            pass

        def predict_proba(self, database):
            pass
