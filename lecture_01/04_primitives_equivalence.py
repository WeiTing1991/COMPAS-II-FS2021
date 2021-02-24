from compas.geometry import Frame
from compas.geometry import Plane
from compas.geometry import Point
from compas.geometry import Polygon
from compas.geometry import Polyline
from compas.geometry import Vector

# Point
assert [0, 5, 1] == Point(0, 5, 1)

# Vector
assert [0, 0, 1] == Vector(0, 0, 1)

# Plane
point = [0, 0, 0]
vector = [1, 0, 0]
assert (point, vector) == Plane(point, vector)

# Frame
point = [5, 0, 0]
xaxis = [1, 0, 0]
yaxis = [0, 1, 0]
assert (point, xaxis, yaxis) == Frame(point, xaxis, yaxis)

# Polyline
p1 = [0, 0, 0]
p2 = [1, 0, 0]
p3 = [1, 1, 0]
p4 = [0, 0, 0]
assert [p1, p2, p3, p4] == Polyline([p1, p2, p3, p4])

# Polygon
assert [p1, p2, p3] == Polygon([p1, p2, p3])
