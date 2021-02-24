from compas.geometry import Frame
from compas.geometry import Plane
from compas.geometry import Point
from compas.geometry import Polygon
from compas.geometry import Polyline
from compas.geometry import Vector

# Point, Vector & Plane
point  = Point(0, 0, 0)
vector = Vector(0, 0, 1)
plane  = Plane(point, vector)
print(point)
print(vector)
print(plane)

# Frame
xaxis = [1, 0, 0]
yaxis = [0, 1, 0]
frame = Frame(point, xaxis, yaxis)
print(frame)

# Polyline
p1 = [0, 0, 0]
p2 = [1, 0, 0]
p3 = [1, 1, 0]
p4 = [0, 0, 0]
polyline = Polyline([p1, p2, p3, p4])
print(polyline)

# Polygon
polygon = Polygon([p1, p2, p3])
print(polygon)
