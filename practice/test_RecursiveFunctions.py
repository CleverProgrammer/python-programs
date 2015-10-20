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

    def test_iterative_number_of_threes(self):
        self.assertEqual(iterative_number_of_threes(3567333), 4, "test recursive number of threes")
        self.assertEqual(iterative_number_of_threes(35465793367333), 6, "test recursive number of threes")

    def test_recursive_number_of_threes(self):
        self.assertEqual(recursive_number_of_threes(3567333), 4, "test recursive number of threes")
        self.assertEqual(recursive_number_of_threes(35465793367333), 6, "test recursive number of threes")

    def test_iterative_is_member(self):
        self.assertEqual(iterative_is_member(['hello','cat','bob'], 'bob'), True, "test iterative is member")
        self.assertEqual(iterative_is_member(['hello','cat','bob'], 'dog'), False, "test iterative is member")

    def test_recursive_is_member(self):
        self.assertEqual(recursive_is_member(['hello','cat','bob'], 'bob'), True, "test recursive is member")
        self.assertEqual(recursive_is_member(['hello','cat','bob'], 'dog'), False, "test recursive is member")

    def test_iterative_remove_x(self):
        self.assertEqual(iterative_remove_x('catxxdogx'), 'catdog', "test iterative remove x")
        self.assertEqual(iterative_remove_x('xxx'), '', "test iterative remove x")

    def test_recursive_remove_x(self):
        self.assertEqual(recursive_remove_x('catxxdogx'), 'catdog', "test recursive remove x")
        self.assertEqual(recursive_remove_x('xxx'), '', "test recursive remove x")

    def test_iterative_insert_x(self):
        self.assertEqual(iterative_insert_x('hel'), 'hxexl', "test iterative insert x")
        self.assertEqual(iterative_insert_x('catdog'), 'cxaxtxdxoxg', "test iterative insert x")

    def test_recursive_insert_x(self):
        self.assertEqual(recursive_insert_x('hel'), 'hxexl', "test recursive insert x")
        self.assertEqual(recursive_insert_x('catdog'), 'cxaxtxdxoxg', "test recursive insert x")
