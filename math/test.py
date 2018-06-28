import unittest
from vector import Vector

class TestCase(unittest.TestCase):

    def test_equality(self):
        assertEqual(Vector(2, 4), Vector(2, 4))

    def test_addition(self):
        sum = Vector(2, 3) + Vector(2, 3)
        assertEqual(sum, Vector(4, 6))

    def test_scalar_mul(self):
        v1 = Vector(1, 9)
        assertEqual(v1 * 3, Vector(3, 27))

    def test_hypotenuse(self):
        v1 = Vector(5, 12)
        assertEqual(13, abs(v1))
    
    def test_null_vector(self):
        v1 = Vector(0, 0)
        assertFalse(bool(abs(v1)))
