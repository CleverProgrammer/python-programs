#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2015-09-22 06:24:38
# @Author  : Rafeh Qazi (rafehqazi1@gmail.com)
# @Link    : rafeh01.github.io/data-science

import unittest


def add(x, y):
    return x + y


class ClassName(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(4, 3), 7)


suite = unittest.TestLoader().loadTestsFromTestCase(ClassName)
unittest.TextTestRunner(verbosity=2).run(suite)
