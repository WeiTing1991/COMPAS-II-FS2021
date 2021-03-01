"""Example: pre- vs. post- multiplication
"""
import math
from compas.geometry import Translation
from compas.geometry import Rotation
from compas.geometry import Scale

R = Rotation.from_axis_and_angle([0, 0, 1], math.radians(30))
T = Translation.from_vector([2, 0, 0])
S = Scale.from_factors([0.5] * 3)
X1 = S * T * R
X2 = R * T * S

print(X1)
print(X2)
print(X1 == X2) # should not be the same!
