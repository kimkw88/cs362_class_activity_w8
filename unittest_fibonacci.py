# CS362_Winter21
# Class Activity
# Program: test_fibonacci.py
# Author: Kwanghyuk Kim

import pytest
import unittest
import fibonacci as f

class FibonacciTests(unittest.TestCase):
    def test_type_true(self):
        self.assertTrue(type(f.fibonacci(4)) is int)
    def test_equal(self):
        self.assertEqual(f.fibonacci(4), 3)
    def test_greater(self):
        self.assertGreater(f.fibonacci(4), 0)

if __name__ == '__main__':
    unittest.main(verbosity=2)

