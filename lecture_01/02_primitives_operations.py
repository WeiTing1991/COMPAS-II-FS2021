from compas.geometry import Point
from compas.geometry import Vector

# Point
p1  = Point(1, 2, 3)
assert p1 ** 3 == [1, 8, 27]
assert p1 + [0, 2, 1] == [1, 4, 4]

# Vector
u = Vector(1, 0, 0)
v = Vector(0, 1, 0)
assert u + v == [1, 1, 0]
assert u.dot(v) == 0.0
assert u.cross(v) == [0, 0, 1]
assert (u * 2).unitized() == [1, 0, 0]

