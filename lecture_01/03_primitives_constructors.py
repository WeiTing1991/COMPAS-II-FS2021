from compas.geometry import Frame
from compas.geometry import Plane
from compas.geometry import Vector

a = Vector(1, 0, 0)
b = Vector.from_start_end([1, 0, 0], [2, 0, 0])
assert a == b

a = Plane([0, 0, 0], [0, 0, 1])
b = Plane.from_three_points([0, 0, 0], [1, 0, 0], [0, 1, 0])
assert a == b

a = Frame([0, 0, 0], [3, 0, 0], [0, 2, 0])
b = Frame.from_points([0, 0, 0], [5, 0, 0], [1, 2, 0])
assert a == b
