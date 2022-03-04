
"""
Exercise 1: Object-Oriented Programming
Write a Python class named Circle constructed by a radius and two methods that
    will compute the area and the perimeter of a circle.

Take 10 minutes to implement the Circle class with two properties and two methods.
Then tests were added. Run doctest:

    python3 -m doctest ex1_oop.py

>>> Circle(3)
<Circle r=3 a=28.274333882308138 p=18.84955592153876>
>>> Circle(5)
<Circle r=5 a=78.53981633974483 p=31.41592653589793>
>>> Circle(1)
<Circle r=1 a=3.141592653589793 p=6.283185307179586>
>>> Circle(1.5)
<Circle r=1.5 a=7.0685834705770345 p=9.42477796076938>
>>> Circle(-1)
Traceback (most recent call last):
  File "ex1_oop.py", line 47, in <module>
    circle4 = Circle(-1)
  File "ex1_oop.py", line 16, in __init__
    assert radius >= 0 # Radius must be greater than zero.
AssertionError

"""
from math import pi

class Circle:
    """Instances of this Circle class has two methods:
                    compute_area() and compute_perimeter()."""
    def __init__(self, radius):
        assert radius >= 0 # Radius must be greater than zero.
        self.radius = radius
    def compute_area(self):
        r = self.radius
        a = pi * r * r # alternatively r**2
        return a
    def compute_perimeter(self):
        r = self.radius
        l = 2 * pi * r
        return l
    @property
    def area(self):
        """Returns the area of this circle, which is PI x RADIUS^2."""
        return self.compute_area()
    @property
    def perimeter(self):
        """Returns the perimeter of this circle, which is 2 x PI x RADIUS."""
        return self.compute_perimeter()
    def __repr__(self):
        return """<Circle r={radius} a={area} p={perimeter}>""".format(
                radius=self.radius,
                area=self.area,
                perimeter=self.perimeter)

if __name__ == '__main__':
    circle1 = Circle(3)
    print(circle1)
    circle2 = Circle(5)
    print(circle2)
    circle3 = Circle(1)
    print(circle3)
    circle4 = Circle(-1)
    print(circle4)
    circle5 = Circle(1.5)
    print(circle5)
