# CS362_Winter21
# Class Activity
# Program: test_factorial.py
# Author: Kwanghyuk Kim

import pytest
from fibonacci import *


def test_fibonacci_equals_1():
    assert fibonacci(2) == 1

def test_fibonacci_equals_2():
    assert fibonacci(3) == 2

def test_fibonacci_equals_3():
    assert fibonacci(4) == 3



def test_factorial_equals_4():
    assert factorial(4) == 24

def test_factorial_equals_5():
    assert factorial(5) == 121