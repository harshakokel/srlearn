# Copyright © 2017-2020 Alexander L. Hayes

"""
Tests for srlearn.mln.BoostedMLN
"""

import pytest
import numpy as np
from numpy.testing import assert_array_almost_equal
from numpy.testing import assert_array_equal
from srlearn.mln import BoostedMLN
from srlearn.background import Background
from srlearn import example_data


def test_initialize_mln_1():
    """Initialize an MLN with default parameters."""
    _mln = BoostedMLN()
    assert _mln.target == "None"
    assert _mln.n_estimators == 10


@pytest.mark.parametrize("test_input", [4, 10, 20])
def test_initialize_mln_trees(test_input):
    """Initialize an MLN with various tree numbers."""
    _mln = BoostedMLN(n_estimators=test_input)
    assert _mln.n_estimators == test_input


@pytest.mark.parametrize(
    "test_input", [0, -1, 1, 4, None, bool, int, 1.5, "None", True]
)
def test_initialize_bad_target(test_input):
    _mln = BoostedMLN(target=test_input)
    with pytest.raises(ValueError):
        _mln.fit(example_data.train)


@pytest.mark.parametrize(
    "test_input", [0, -1, None, bool, int, 1.5, "None", "True", True, 3.3]
)
def test_initialize_bad_n_estimators(test_input):
    """Test bad values for n_estimators"""
    _mln = BoostedMLN(target="cancer", background=Background(), n_estimators=test_input)
    with pytest.raises(ValueError):
        _mln.fit(example_data.train)


@pytest.mark.parametrize("test_input", [1, 2, 3, 4, 5])
def test_learn_example_dataset_1(test_input):
    """Learn from the example database."""
    _bk = Background(modes=example_data.train.modes, use_std_logic_variables=True)
    _mln = BoostedMLN(background=_bk, target="cancer", n_estimators=test_input)
    _mln.fit(example_data.train)
    assert len(_mln.estimators_) == test_input
