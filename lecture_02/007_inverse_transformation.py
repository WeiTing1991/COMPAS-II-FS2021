"""Example: Transform a point and invert the transformation
"""
from compas.geometry import Point
from compas.geometry import Rotation
from math import pi

p = Point(3, 4, 5)
T = Rotation.from_axis_and_angle([2, 2, 2], pi/4)

p.transform(T)  # transform Point p with T
print(p)

Tinv = T.inverse()  # create inverse Transformation to T

p.transform(Tinv)  # transform Point p with inverse Transformation

# check if p has the same values as in the beginning
print(p)  # == (3, 4, 5)

# Btw, what is the result of multiplying T with Tinv?
print(T * Tinv)
