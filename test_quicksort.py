#! /usr/bin/env python2.7
# encoding:utf-8

""" quicksort 的测试
"""

import unittest
import random
from quicksort import QuickSort


class TestQuickSort(unittest.TestCase):
    """ quicksort 的测试用例
    """

    def setUp(self):
        self.qs = QuickSort()

    def tearDown(self):
        self.qs = None

    def testCommon(self):
        assert self.qs.sort((2, 4, 1, 3)) == [1, 2, 3, 4]

    def testBoundary(self):
        assert self.qs.sort(()) == []

    def testSingle(self):
        assert self.qs.sort((1,)) == [1,]

    def testEqu(self):
        assert self.qs.sort((1, 1)) == [1, 1]

    def testNeg(self):
        assert self.qs.sort((1, -1)) == [-1, 1]

    def testRandom(self):
        data = list()

        for i in range(1, 100):
            data.append(random.randint(1, 10000))

        qdata = data[:]
        data.sort()

        assert self.qs.sort(tuple(qdata)) == data


if __name__ == "__main__":
    unittest.main()
