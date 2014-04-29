#! /usr/bin/env python2.7

""" My test calss
"""

class Add(object):
    """ A sample ADD calculator class for test
    """

    def __init__(self):
        self.i = 0
        self.j = 0

    def calc(self, i, j):
        """ just do a ADD calc
        """

        self.i = i
        self.j = j
        return self.i+self.j
