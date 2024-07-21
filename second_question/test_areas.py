import unittest
from math import pi
from libForArea import Area


class TestAreas(unittest.TestCase):
    e = Area()

    def test_area(self):
        self.assertEqual(self.e.circle(12), 12 ** 2 * pi)
        self.assertEqual(self.e.circle(123), 123 ** 2 * pi)
        self.assertEqual(self.e.circle(1255213), 1255213 ** 2 * pi)
        self.assertEqual(self.e.circle(0), 0)
        self.assertEqual(self.e.circle(1), pi)
        self.assertEqual(self.e.triangle(12, 10, 8),
                         (15*(15-12)*(15-10)*(15-8))**.5)
        self.assertEqual(self.e.triangle(17, 10, 9),
                         (18*(18-17)*(18-10)*(18-9))**.5)
        self.assertEqual(self.e.triangle(0, 0, 0), 0)

    def test_values(self):
        self.assertRaises(ValueError, self.e.circle, -1)
        self.assertRaises(ValueError, self.e.circle, -10000)
        self.assertRaises(ValueError, self.e.triangle, 10, 2, 3)
        self.assertRaises(ValueError, self.e.triangle, -3, 10, 12)

    def test_types(self):
        self.assertRaises(TypeError, self.e.circle, [123, 123, 123])
        self.assertRaises(TypeError, self.e.circle, "hello")
        self.assertRaises(TypeError, self.e.triangle,
                          [123, 123, 123], "wsf", 123)
        self.assertRaises(TypeError, self.e.triangle, "hello", {123, 123}, 123)
