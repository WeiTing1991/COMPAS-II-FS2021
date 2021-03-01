"""Change-basis transformation vs transformation between two frames.
"""
from compas.geometry import Point
from compas.geometry import Frame
from compas.geometry import Transformation

F1 = Frame([2, 2, 2], [0.12, 0.58, 0.81], [-0.80, 0.53, -0.26])
F2 = Frame([1, 1, 1], [0.68, 0.68, 0.27], [-0.67, 0.73, -0.15])

# transformation between 2 frames F1, F2
Tf = Transformation.from_frame_to_frame(F1, F2)
# change-basis transformation between two frames F1 and F2.
Tc = Transformation.from_change_of_basis(F1, F2)

# they are different
print(Tf)
print(Tc)

# This is how to use Tf: transform geometry into another coordinate frame
pt = Point(2, 2, 2)
pt.transform(Tf)
print(pt, "==", F2.point)

# This is how to use Tc: represent geometry in another coordinate frame
pt = Point(0, 0, 0)  # local point in F1
pt.transform(Tc)
print(pt, "==", F2.to_local_coordinates(F1.point))
