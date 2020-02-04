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

    # pylint: disable=too-many-instance-attributes

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

        self._check_params()

        # Write the background to a file.
        self.background.write(
            filename="train", location=self.file_system.files.TRAIN_DIR.value
        )

        # Write the data to files.
        database.write(
            filename="train", location=self.file_system.files.TRAIN_DIR.value
        )

        _CALL = (
            "java -jar "
            + str(self.file_system.files.BOOST_JAR.value)
            + " -l -mln -train "
            + str(self.file_system.files.TRAIN_DIR.value)
            + " -target "
            + self.target
            + " -trees "
            + str(self.n_estimators)
            + " > "
            + str(self.file_system.files.TRAIN_LOG.value)
        )

        if self.debug:
            print(_CALL)

        # Call the constructed command.
        self._call_shell_command(_CALL)

        # Read the trees from files.
        _estimators = []
        for _tree_number in range(self.n_estimators):
            with open(
                self.file_system.files.TREES_DIR.value.joinpath(
                    "{0}Tree{1}.tree".format(self.target, _tree_number)
                )
            ) as _fh:
                _estimators.append(_fh.read())

        self.estimators_ = _estimators

        return self

    def _run_inference(self, database) -> None:
        """Run inference mode on the BoostSRL Jar files.

        This is a helper method for ``self.predict`` and ``self.predict_proba``
        """
        return

    def predict(self, database):
        return

    def predict_proba(self, database):
        return
