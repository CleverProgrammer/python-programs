__author__ = 'Rafeh'
from unittest import TestCase
from practice_activity import *


class TestRecursiveVsIterativeFunctions(TestCase):
    def test_iterative_double(self):
        self.assertEqual(iterative_double(4), 8, "test iterative double")
        self.assertEqual(iterative_double(10), 20, "test iterative double")

    def test_recursive_double(self):
        self.assertEqual(recursive_double(4), 8, "test recursive double")
        self.assertEqual(recursive_double(10), 20, "test recursive double")

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
        self.assertEqual(iterative_is_member(['hello', 'cat', 'bob'], 'bob'), True, "test iterative is member")
        self.assertEqual(iterative_is_member(['hello', 'cat', 'bob'], 'dog'), False, "test iterative is member")

    def test_recursive_is_member(self):
        self.assertEqual(recursive_is_member(['hello', 'cat', 'bob'], 'bob'), True, "test recursive is member")
        self.assertEqual(recursive_is_member(['hello', 'cat', 'bob'], 'dog'), False, "test recursive is member")

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

    def test_iterative_list_reverse(self):
        self.assertEqual(iterative_list_reverse([2, 3, 1]), [1, 3, 2], "test iterative list reverse")
        self.assertEqual(iterative_list_reverse([5, 2, 7, 6]), [6, 7, 2, 5], "test iterative list reverse")

    def test_recursive_list_reverse(self):
        self.assertEqual(recursive_list_reverse([2, 3, 1]), [1, 3, 2], "test recursive list reverse")
        self.assertEqual(recursive_list_reverse([5, 2, 7, 6]), [6, 7, 2, 5], "test recursive list reverse")

    def test_recursive_anagrams(self):
        word = 'hello'
        expected = ['hello', 'ehllo', 'elhlo', 'ellho', 'elloh', 'hlelo', 'lhelo', 'lehlo', 'lelho', 'leloh',
                    'hlleo', 'lhleo', 'llheo', 'lleho', 'lleoh', 'hlloe', 'lhloe', 'llhoe', 'llohe', 'lloeh',
                    'hello', 'ehllo', 'elhlo', 'ellho', 'elloh', 'hlelo', 'lhelo', 'lehlo', 'lelho', 'leloh',
                    'hlleo', 'lhleo', 'llheo', 'lleho', 'lleoh', 'hlloe', 'lhloe', 'llhoe', 'llohe', 'lloeh',
                    'helol', 'ehlol', 'elhol', 'elohl', 'elolh', 'hleol', 'lheol', 'lehol', 'leohl', 'leolh',
                    'hloel', 'lhoel', 'lohel', 'loehl', 'loelh', 'hlole', 'lhole', 'lohle', 'lolhe', 'loleh',
                    'helol', 'ehlol', 'elhol', 'elohl', 'elolh', 'hleol', 'lheol', 'lehol', 'leohl', 'leolh',
                    'hloel', 'lhoel', 'lohel', 'loehl', 'loelh', 'hlole', 'lhole', 'lohle', 'lolhe', 'loleh',
                    'heoll', 'eholl', 'eohll', 'eolhl', 'eollh', 'hoell', 'ohell', 'oehll', 'oelhl', 'oellh',
                    'holel', 'ohlel', 'olhel', 'olehl', 'olelh', 'holle', 'ohlle', 'olhle', 'ollhe', 'olleh',
                    'heoll', 'eholl', 'eohll', 'eolhl', 'eollh', 'hoell', 'ohell', 'oehll', 'oelhl', 'oellh',
                    'holel', 'ohlel', 'olhel', 'olehl', 'olelh', 'holle', 'ohlle', 'olhle', 'ollhe', 'olleh']
        self.assertEqual(recursive_anagrams(word), expected, "test recursive anagrams")

    def test_iterative_exponents(self):
        self.assertEqual(iterative_exponents(4, 2), 16, 'test iterative fast exponentiation')
        self.assertEqual(iterative_exponents(8, 2), 64, 'test iterative fast exponentiation')

    def test_recursive_exponents(self):
        self.assertEqual(recursive_exponents(4, 2), 16, 'test iterative fast exponentiation')
        self.assertEqual(recursive_exponents(8, 2), 64, 'test iterative fast exponentiation')

    def test_recursive_fibonacci(self):
        self.assertEqual(recursive_fibonacci(6), 8, 'test recursive fibonacci')

    def test_recursive_selection_sort(self):
        self.assertEqual(recursive_selection_sort([7, 6, 5]), [5, 6, 7], 'test recursive selection sort')
        from random import randrange
        unsorted_random_list = [randrange(1, 100) for i in range(100)]
        sorted_random_list = sorted(unsorted_random_list)
        self.assertEqual(recursive_selection_sort(unsorted_random_list), sorted_random_list, 'test recursive selection')
        self.assertEqual(recursive_selection_sort([6, 7, 4, 2]), [2, 4, 6, 7], 'test recursive selection sort')

    def test_recursive_merge_sort(self):
        self.assertEqual(recursive_merge_sort([6,7,2,5]), [2,5,6,7], 'test merge')

    def test_recursive_binary_search(self):
        self.assertEqual(recursive_binary_search([1,2,3], 3), True)
        self.assertEqual(recursive_binary_search([5,8,9,25,99,358,359], 9),True)
        self.assertEqual(recursive_binary_search([5,8,9,25,99,358,359], 358), True)
        self.assertEqual(recursive_binary_search([5,8,9,25,99,358,359], 26), False)
