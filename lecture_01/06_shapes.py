from compas.geometry import Box
from compas.geometry import Circle
from compas.geometry import Cylinder
from compas.geometry import Frame
from compas.geometry import Plane
from compas.geometry import Sphere

# Box
b1 = Box(Frame.worldXY(), 5, 1, 3)          # xsize, ysize, zsize
b2 = Box.from_width_height_depth(5, 3, 1)   # width=xsize, height=zsize, depth=ysize
assert str(b1) == str(b2)
print(b1)

# Sphere
s1 = Sphere([0, 0, 0], 5)
print(s1)

# Cylinder
plane = Plane([0, 0, 0], [0, 0, 1])
circle = Circle(plane, 5)
c1 = Cylinder(circle, height=4)
print(c1)
