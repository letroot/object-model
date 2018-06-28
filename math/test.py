"""Vector class test suite"""

import unittest

from vectors import Vector


class TestCase(unittest.TestCase):

    def test_equality(self):
        """Test equality."""
        self.assertEqual(Vector(2, 4), Vector(2, 4))

    def test_addition(self):
        """Test addition operations."""
        sum_ = Vector(2, 3) + Vector(2, 3)
        self.assertEqual(sum_, Vector(4, 6))

    def test_scalar_mul(self):
        """Test scalar multiplication."""
        v1 = Vector(1, 9)
        self.assertEqual(v1 * 3, Vector(3, 27))

    def test_hypotenuse(self):
        """Test resultant vector."""
        v1 = Vector(5, 12)
        self.assertEqual(13, abs(v1))

    def test_null_vector(self):
        """Zero vectors exist, you know"""
        v1 = Vector(0, 0)
        self.assertFalse(bool(v1))

if __name__ == "__main__":
    unittest.main()
