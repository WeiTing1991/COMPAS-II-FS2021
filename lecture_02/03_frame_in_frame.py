"""Example: 'frame in frame'
"""
from compas.geometry import Point
from compas.geometry import Vector
from compas.geometry import Frame

point = Point(146.00, 150.00, 161.50)
xaxis = Vector(0.9767, 0.0010, -0.214)
yaxis = Vector(0.1002, 0.8818, 0.4609)
F0 = Frame(point, xaxis, yaxis) # coordinate system F0

point = Point(35., 35., 35.)
xaxis = Vector(0.604, 0.430, 0.671)
yaxis = Vector(-0.631, 0.772, 0.074)
f_lcf = Frame(point, xaxis, yaxis) # frame f_lcf in F0 (local coordinates)

# frame in global (world) coordinate system
f_wcf = F0.to_world_coordinates(f_lcf)
print(f_wcf)

f_lcf2 = F0.to_local_coordinates(f_wcf) # world coords back to local coords
print(f_lcf2) # should equal f_lcf
print(f_lcf == f_lcf2)
