#! /usr/bin/env python2.7

""" quicksort 的测试
"""

import unittest
from quicksort import QuickSort


class TestQuickSort(unittest):
    """ quicksort 的测试用例
    """

    def setUp(self):
        self.qs = QuickSort()

    def tearDown(self):
        self.qs = None

    def testCommon(self):
        # 构造测试数据先
        data = (2, 4, 1, 3)
        self.qs = QuickSort(data)
        assert qs.sort() == [1, 2, 3, 4]
