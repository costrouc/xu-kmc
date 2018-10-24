import numpy as np


def test_numpy():
    assert np.sum(np.full((10, 10), 5)) == 500
