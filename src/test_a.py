import pytest
import time
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
    time.sleep(1)
    assert foo(3) == 4

def test_foo1():
    assert foo(3) == 5
 
def test_bar(): 
    assert foo(3) == 4 
