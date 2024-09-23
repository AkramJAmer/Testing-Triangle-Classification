import unittest
import math



def classify_triangle(a, b, c):
  
    if not all(isinstance(x, (int, float)) for x in (a, b, c)):
        return "InvalidTypeInput"
    
    if any(x <= 0 for x in (a, b, c)):
        return "InvalidSizeInput"
    
    
    sides = sorted([a, b, c])
    if sides[0] + sides[1] <= sides[2]:
        return "InvalidSizeInput"
    
    # Identify triangle type based on side lengths
    if a == b == c:
        return "Equilateral"
    
    if a == b or b == c or a == c:

        if is_right_triangle(a, b, c):
            return "Isosceles Right"
        return "Isosceles"
    
    if is_right_triangle(a, b, c):
        return "Right"
    
    return "Scalene"


def is_right_triangle(a, b, c):
    
    a, b, c = sorted([a, b, c])
    return math.isclose(a ** 2 + b ** 2, c ** 2)


def run_classify_triangle(a, b, c):
    result = classify_triangle(a, b, c)
    print(f'classify_triangle({a}, {b}, {c}) = {result}')


class TestTriangle(unittest.TestCase):
    def test_invalid_inputs(self):
        # Test for invalid inputs
        self.assertEqual(classify_triangle(1, 1, 4), 'InvalidSizeInput', 'Invalid side lengths')
        self.assertEqual(classify_triangle(0, 2, 3), 'InvalidSizeInput', 'Zero or negative input')
        self.assertEqual(classify_triangle(-1, 1, 1), 'InvalidSizeInput', 'Negative side length')
        self.assertEqual(classify_triangle(2, "3", 5), 'InvalidTypeInput', 'Invalid type (string input)')
    
    def test_triangle_classification(self):
        # Test for correct classification of triangles
        self.assertEqual(classify_triangle(1, 1, 1), 'Equilateral', 'Equilateral triangle test')
        self.assertEqual(classify_triangle(3, 4, 5), 'Right', 'Right triangle test')
        self.assertEqual(classify_triangle(3, 3, 4), 'Isosceles', 'Isosceles triangle test')
        self.assertEqual(classify_triangle(5, 6, 7), 'Scalene', 'Scalene triangle test')
    
    def test_combined_cases(self):
        # Test for combination cases, like isosceles right triangles
        self.assertEqual(classify_triangle(1, 1, math.sqrt(2)), 'Isosceles Right', 'Isosceles Right triangle test')
        self.assertNotEqual(classify_triangle(10, 10, 10), 'Isosceles', 'Equilateral triangle misclassification')
        self.assertNotEqual(classify_triangle(3, 4, 5), 'Equilateral', 'Right triangle misclassification')
        self.assertNotEqual(classify_triangle(3, 3, 4), 'Scalene', 'Isosceles triangle misclassification')


if __name__ == '__main__':
    run_classify_triangle(1, 2, 3)
    run_classify_triangle(1, 1, 1)
    run_classify_triangle(3, 4, 5)
    run_classify_triangle(0, 1, 2)
    run_classify_triangle(1, 1, math.sqrt(2))

    unittest.main(exit=False)
