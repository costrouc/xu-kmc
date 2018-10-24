import numpy as np

from kmc import example


def test_addition():
    assert 1 + 1 == 2


def test_numpy_sum():
    assert np.sum(np.full((10, 10), 5)) == 500


def test_example_do_work_add():
    assert example.do_work_sum(1, 10) == 11


def test_foobar_hello_world():
    foobar = example.FooBar("asdf", "qwer")
    assert foobar.hello_world() == "asdf Hello World! qwer"
