pie = 3.141592653589793238462643383279502884197


def area_of_triangle(base, height):
    return (base * height) / 2


def area_of_circle(radius):
    return pie * radius ** 2


def area_of_rectangle(length, width):
    return length * width


def area_of_square(side):
    return side ** 2


def area_of_parallelogram(base, height):
    return base * height


def area_of_trapezoid(base1, base2, height):
    return ((base1 + base2) / 2) * height


def area_of_ellipse(major_axis, minor_axis):
    return pie * major_axis * minor_axis


def area_of_rhombus(diagonal1, diagonal2):
    return (diagonal1 * diagonal2) / 2


def area_of_regular_polygon(perimeter, apothem):
    return (perimeter * apothem) / 2


def area_of_sector(radius, angle):
    return (angle / 360) * pie * radius ** 2


def area_of_equilateral_triangle(side):
    return (side ** 2 * 3 ** 0.5) / 4


def area_of_isosceles_triangle(base, height):
    return (base * height) / 2
