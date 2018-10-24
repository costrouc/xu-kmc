"""Example module that will be deleted in the future

This file demonstates proper coding conventions along with how to
document your functions and classes. The docstring format that we are
using is numpy docstrings
https://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_numpy.html

"""


def do_work_sum(a, b):
    """Add the sum of two variables

    Parameters
    ----------
    a: int
      first integer as input
    b: int
      second integer as input

    Returns
    -------
    int
      sum of a and b

    Example
    -------
    Examples should be written in doctest format, and should
    illustrate how to use the function.

    >>> print(do_work_sum(1, 3))
    4
    """
    return a + b


class FooBar:
    """Essential to the opperation of the example class

    The __init__ method should be documented in either the class level
    docstring.

    Note
    ----
    Do not include the `self` parameter in the ``Parameters`` section.

    Parameters
    ----------
    biz: str
      special string to start sentences with
    baz: str
      special string to end sentences with
    """
    def __init__(self, biz, baz):
        self.biz = biz
        self.baz = baz

    def hello_world(self):
        """Print hello world message with biz baz addition"""
        return self.biz + " Hello World! " + self.baz
