#! /usr/bin/env python2.7

import unittest
from cbt_add import Add

class AddTestCase(unittest.TestCase):
    """ My first Python Unittext case.
    """

    def setUp(self):
        self.add = Add()

    def tearDown(self):
        self.add = None

    def testAdd(self):
        assert self.add.calc(1, 2) == 3

    def testAddNeg(self):
        assert self.add.calc(1, -2) == -1


if __name__ == "__main__":
    unittest.main()
