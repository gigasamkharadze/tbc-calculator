def circle_area(r):
    return 3.14 * r ** 2


def circle_circumference(r):
    return 2 * 3.14 * r


def triangle_perimeter(a, b, c):
    return a + b + c


def triangle_area(a, b, c):
    s = (a + b + c) / 2
    area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
    return area


def rectangle_area(a, b):
    return a * b


def rectangle_perimeter(a, b):
    return 2 * (a + b)


def trapezoid_area(a, b, c):
    return (a + b) * c / 2


def trapezoid_perimeter(a, b, c, d):
    return a + b + c + d
