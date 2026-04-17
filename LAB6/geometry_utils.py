import math

def validate_positive(*args):
    for arg in args:
        if arg <= 0:
            raise ValueError("Dimensions must be strictly positive.")

def circle_area(radius):
    validate_positive(radius)
    return math.pi * (radius ** 2)

def circle_perimeter(radius):
    validate_positive(radius)
    return 2 * math.pi * radius

def rectangle_area(width, height):
    validate_positive(width, height)
    return width * height

def rectangle_perimeter(width, height):
    validate_positive(width, height)
    return 2 * (width + height)

def triangle_area(base, height):
    validate_positive(base, height)
    return 0.5 * base * height