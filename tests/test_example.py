from kmc import example


def test_addition():
    assert 1 + 1 == 2


def test_example_do_work_add():
    assert example.do_work_sum(1, 10) == 11
