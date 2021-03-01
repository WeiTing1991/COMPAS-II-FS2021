"""Example: Pre-multiply transformations
"""
from compas.geometry import Point
from compas.geometry import Translation
from compas.geometry import Rotation
from compas.geometry import Scale
from compas.geometry import allclose

p = Point(1, 1, 1)

translation = [1, 2, 3]
A = Translation.from_vector(translation)  # create Translation
axis, angle = [-0.8, 0.35, 0.5], 2.2
B = Rotation.from_axis_and_angle(axis, angle)  # create Rotation
scale_factors = [0.1, 0.3, 0.4]
C = Scale.from_factors(scale_factors)  # create Scale

# Transform p1 one by one
p1 = p.copy()
p1.transform(A)
p1.transform(B)
p1.transform(C)

# Transform with only one concatenated matrix
p2 = p.copy()
p2.transform(C * B * A)

# p1 == p2 ?
print(allclose(p1, p2))