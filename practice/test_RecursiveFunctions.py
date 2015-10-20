__author__ = 'Rafeh'
from unittest import TestCase
from recursive_vs_iterative import *

class TestRecursiveFunctions(TestCase):
    def test_iterative_double(self):
        self.assertEqual(iterative_double(4), 8, "test iterative double" )

    def test_recursive_double(self):
        self.assertEqual(recursive_double(4), 8, "test recursive double" )

    def test_iterative_sum_up_to(self):
        self.assertEqual(iterative_sum_up_to(3), 6, "test iterative sum up to")
        self.assertEqual(iterative_sum_up_to(100), 5050, "test iterative sum up to")

    def test_recursive_sum_up_to(self):
        self.assertEqual(recursive_sum_up_to(3), 6, "test recursive sum up to")
        self.assertEqual(recursive_sum_up_to(100), 5050, "test recursive sum up to")
