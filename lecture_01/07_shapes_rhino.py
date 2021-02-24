from compas_rhino.artists import BoxArtist
from compas_rhino.artists import CylinderArtist
from compas_rhino.artists import SphereArtist

from compas.geometry import Box
from compas.geometry import Circle
from compas.geometry import Cylinder
from compas.geometry import Frame
from compas.geometry import Plane
from compas.geometry import Sphere

# Box
b1 = Box(Frame.worldXY(), 10, 1, 4)          # xsize, ysize, zsize
b2 = Box.from_width_height_depth(10, 4, 1)   # width=xsize, height=zsize, depth=ysize
assert str(b1) == str(b2)
print(b1)

# Sphere
s1 = Sphere([10, 0, 0], 4)
print(s1)

# Cylinder
plane = Plane([20, 0, 0], [0, 0, 1])
circle = Circle(plane, 5)
c1 = Cylinder(circle, height=4)
print(c1)

# Draw!
artist = BoxArtist(b1, layer='shapes')
artist.draw()

artist = SphereArtist(s1, layer='shapes')
artist.draw()

artist = CylinderArtist(c1, layer='shapes')
artist.draw()
