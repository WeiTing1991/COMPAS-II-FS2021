import math

from compas.geometry import Point
from compas.geometry import Quaternion
from compas.geometry import Rotation
from compas.geometry import Transformation
from compas.geometry import Translation

# transform with identity matrix
x = Transformation()
a = Point(1, 0, 0)
b = a.transformed(x)
assert a == b

# translate
t = Translation.from_vector([5, 1, 0])
b = a.transformed(t)
assert b == [6, 1, 0]

# in-place transform
r = Rotation.from_axis_and_angle([0, 0, 1], math.pi)
a.transform(r)
assert str(a) == str(Point(-1.0, 0.0, 0.0))

# rotation from quaternion
q = Quaternion(0.918958, -0.020197, -0.151477, 0.363544)
assert q.is_unit

R = Rotation.from_quaternion(q)
assert R.quaternion == q
