import unittest
from areaofShapesLib import *


class TestAreaFunctions(unittest.TestCase):

    def test_area_of_triangle_with_positive_values(self):
        self.assertEqual(area_of_triangle(10, 5), 25)

    def test_area_of_triangle_with_zero_values(self):
        self.assertEqual(area_of_triangle(0, 5), 0)

    def test_area_of_circle_with_positive_value(self):
        self.assertAlmostEqual(area_of_circle(5), 78.53981633974483)

    def test_area_of_circle_with_zero_value(self):
        self.assertEqual(area_of_circle(0), 0)

    def test_area_of_rectangle_with_positive_values(self):
        self.assertEqual(area_of_rectangle(5, 10), 50)

    def test_area_of_rectangle_with_zero_values(self):
        self.assertEqual(area_of_rectangle(0, 10), 0)

    def test_area_of_square_with_positive_value(self):
        self.assertEqual(area_of_square(5), 25)

    def test_area_of_square_with_zero_value(self):
        self.assertEqual(area_of_square(0), 0)

    def test_area_of_parallelogram_with_positive_values(self):
        self.assertEqual(area_of_parallelogram(5, 10), 50)

    def test_area_of_parallelogram_with_zero_values(self):
        self.assertEqual(area_of_parallelogram(0, 10), 0)

    def test_area_of_trapezoid_with_positive_values(self):
        self.assertEqual(area_of_trapezoid(5, 10, 5), 37.5)

    def test_area_of_trapezoid_with_zero_values(self):
        self.assertEqual(area_of_trapezoid(0, 10, 5), 25)

    def test_area_of_ellipse_with_positive_values(self):
        self.assertAlmostEqual(area_of_ellipse(5, 10), 157.07963267948966)

    def test_area_of_ellipse_with_zero_values(self):
        self.assertEqual(area_of_ellipse(0, 10), 0)

    def test_area_of_rhombus_with_positive_values(self):
        self.assertEqual(area_of_rhombus(5, 10), 25)

    def test_area_of_rhombus_with_zero_values(self):
        self.assertEqual(area_of_rhombus(0, 10), 0)

    def test_area_of_regular_polygon_with_positive_values(self):
        self.assertEqual(area_of_regular_polygon(5, 10), 25)

    def test_area_of_regular_polygon_with_zero_values(self):
        self.assertEqual(area_of_regular_polygon(0, 10), 0)

    def test_area_of_sector_with_positive_values(self):
        self.assertAlmostEqual(area_of_sector(5, 90), 19.634954084936208)

    def test_area_of_sector_with_zero_values(self):
        self.assertEqual(area_of_sector(0, 90), 0)

    def test_area_of_equilateral_triangle_with_positive_value(self):
        self.assertAlmostEqual(area_of_equilateral_triangle(5), 10.825317547305483)

    def test_area_of_equilateral_triangle_with_zero_value(self):
        self.assertEqual(area_of_equilateral_triangle(0), 0)

    def test_area_of_isosceles_triangle_with_positive_values(self):
        self.assertEqual(area_of_isosceles_triangle(5, 10), 25)

    def test_area_of_isosceles_triangle_with_zero_values(self):
        self.assertEqual(area_of_isosceles_triangle(0, 10), 0)


if __name__ == '__main__':
    unittest.main()
