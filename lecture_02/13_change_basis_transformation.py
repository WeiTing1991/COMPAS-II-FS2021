"""Change-basis transformation.
"""
from compas.geometry import Point
from compas.geometry import Frame
from compas.geometry import Transformation

F1 = Frame.worldXY()
F2 = Frame([1.5, 1, 0], [0.68, 0.68, 0.27], [-0.67, 0.73, -0.15])
P = Point(2, 2, 2)  # local point in F1

# change-basis transformation between two frames F1 and F2.
T = Transformation.from_change_of_basis(F1, F2)

# Represent geometry (=point P) in another coordinate frame
print(P.transformed(T))
# You can also use the following
print(F2.to_local_coordinates(P))
