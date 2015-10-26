from unittest import TestCase
from word_wrangler import *

__author__ = 'Rafeh'


class Test_Word_Wrangler(TestCase):

    def test_merge(self):
        self.assertEqual(merge([1,2], [3,4]), [1, 2, 3, 4], 'test merge')
