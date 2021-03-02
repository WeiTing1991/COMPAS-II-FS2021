"""Transformation between two frames.
"""
from compas.geometry import Point
from compas.geometry import Frame
from compas.geometry import Transformation

F1 = Frame.worldXY()
F2 = Frame([1.5, 1, 0], [0.68, 0.68, 0.27], [-0.67, 0.73, -0.15])
P = Point(2, 2, 2)  # local point in F1

# transformation between 2 frames F1, F2
T = Transformation.from_frame_to_frame(F1, F2)

# Transform geometry (=point P) into another coordinate frame
print(P.transformed(T))
