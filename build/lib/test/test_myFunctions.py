import unittest
from areaofShapesLib import ArithmeticOperations


class ArithmeticOperationsTest(unittest.TestCase):

    def area_of_triangle_positive_values(self):
        result = ArithmeticOperations.area_of_triangle(10, 5)
        self.assertEqual(result, 25)

    def area_of_triangle_zero_values(self):
        result = ArithmeticOperations.area_of_triangle(0, 5)
        self.assertEqual(result, 0)

    def area_of_circle_positive_values(self):
        result = ArithmeticOperations.area_of_circle(5)
        self.assertEqual(result, 78.53981633974483)

    def area_of_circle_zero_values(self):
        result = ArithmeticOperations.area_of_circle(0)
        self.assertEqual(result, 0)

    def area_of_rectangle_positive_values(self):
        result = ArithmeticOperations.area_of_rectangle(10, 5)
        self.assertEqual(result, 50)

    def area_of_rectangle_zero_values(self):
        result = ArithmeticOperations.area_of_rectangle(0, 5)
        self.assertEqual(result, 0)

    # Continue with the rest of the methods in the same manner


if __name__ == '__main__':
    unittest.main()
