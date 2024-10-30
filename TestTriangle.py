import unittest
from Triangle import classify_triangle

class TestTriangles(unittest.TestCase):

    def test_right_triangle_a(self):
        """Test case for right triangle (a**2 + b**2 = c**2)"""
        self.assertEqual(classify_triangle(3, 4, 5), 'Right')

    def test_right_triangle_b(self):
        """Test case for right triangle (a**2 + c**2 = b**2)"""
        self.assertEqual(classify_triangle(5, 12, 13), 'Right')

    def test_equilateral_triangles(self):
        """Test case for equilateral triangle"""
        self.assertEqual(classify_triangle(5, 5, 5), 'Equilateral')

    def test_scalene_triangle(self):
        """Test case for scalene triangle"""
        self.assertEqual(classify_triangle(4, 5, 6), 'Scalene')

    def test_isosceles_triangle(self):
        """Test case for isosceles triangle"""
        self.assertEqual(classify_triangle(5, 5, 8), 'Isoceles')

    def test_not_a_triangle(self):
        """Test case for invalid triangle (NotATriangle)"""
        self.assertEqual(classify_triangle(1, 2, 10), 'NotATriangle')

    def test_negative_sides(self):
        """Test case for negative side lengths (InvalidInput)"""
        self.assertEqual(classify_triangle(-1, -1, -1), 'InvalidInput')

    def test_zero_sides(self):
        """Test case for zero side lengths (InvalidInput)"""
        self.assertEqual(classify_triangle(0, 0, 0), 'InvalidInput')

    def test_non_integer_sides(self):
        """Test case for non-integer side lengths (InvalidInput)"""
        self.assertEqual(classify_triangle(1.5, 2.5, 3.5), 'InvalidInput')

if __name__ == '__main__':
    unittest.main()
