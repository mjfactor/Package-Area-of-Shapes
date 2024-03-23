class ArithmeticOperations:
    pie = 3.141592653589793238462643383279502884197

    @staticmethod
    def area_of_triangle(base, height):
        return (base * height) / 2

    @classmethod
    def area_of_circle(cls, radius):
        return cls.pie * radius ** 2

    @staticmethod
    def area_of_rectangle(length, width):
        return length * width

    @staticmethod
    def area_of_square(side):
        return side ** 2

    @staticmethod
    def area_of_parallelogram(base, height):
        return base * height

    @staticmethod
    def area_of_trapezoid(base1, base2, height):
        return ((base1 + base2) / 2) * height

    @classmethod
    def area_of_ellipse(cls, major_axis, minor_axis):
        return cls.pie * major_axis * minor_axis

    @staticmethod
    def area_of_rhombus(diagonal1, diagonal2):
        return (diagonal1 * diagonal2) / 2

    @staticmethod
    def area_of_regular_polygon(perimeter, apothem):
        return (perimeter * apothem) / 2

    @classmethod
    def area_of_sector(cls, radius, angle):
        return (angle / 360) * cls.pie * radius ** 2

    @staticmethod
    def area_of_equilateral_triangle(side):
        return (side ** 2 * 3 ** 0.5) / 4

    @staticmethod
    def area_of_isosceles_triangle(base, height):
        return (base * height) / 2