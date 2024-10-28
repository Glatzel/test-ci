import time

import pytest


def foo(x):
    return x + 1


def bar(x):
    return x + 1


def bar1(x):
    return x + 1


def foobar(x):
    return x + 3


@pytest.mark.benchmark
def test_foo():
    sum(1 for x in list(range(1000)) if x % 2 == 0)
    assert foo(3) == 4


def test_bar():
    assert foo(3) == 4
