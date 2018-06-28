# Vector is a rapper too.

"""Here we implement
__add__, __abs__,  __mul__, __repr__

Example: A simple 2-D Vector class
"""
from math import hypot


class Vector:
    """A representation of Vectors."""

    def __init__(self, x=0.0, y=0.0):
        self.x = x
        self.y = y


    def __repr__(self):
        # Why %r? and not f-strings or format?
        return "Vector(%r, %r)" % self.x, self.y
