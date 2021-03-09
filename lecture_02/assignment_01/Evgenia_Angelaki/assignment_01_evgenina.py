
"""Assignment 01: Project box to xy-plane
- Evgenina
"""

"""
IMPORTS
"""
import math as m

from compas.geometry import Box
from compas.geometry import Frame
from compas.geometry import Projection
from compas.geometry import Plane
from compas.datastructures import Mesh

from compas.geometry import Rotation
from compas.geometry import Translation
from compas.geometry import Vector

from compas_rhino.artists import BoxArtist
from compas_rhino.artists import MeshArtist


"""
CREATE AND TRANSFORM FRAME
"""
F = Frame.worldXY() #simple XY frame as a base to transform

#create R transformation
axis, angle = [0.5, 0.5, 0.5], m.radians(60)
R = Rotation.from_axis_and_angle(axis, angle)

print("Rotation:\n", R)

#create T transformation
trans_vector = Vector(10,10,20)
T= Translation.from_vector(trans_vector)

print("Translation:\n", T)

#create concantinated transformation of Frame
X1 = R * T
F.transform(X1)
print(F)


"""
CREATE BOX AND PROJECTION
"""
width, length, height = 1, 1, 8
box = Box(F, width, length, height)

#create projection
projection_plane = Plane([0,0,0], [0,0,1]) #world XY plane
P= Projection.from_plane(projection_plane) #orthogonal projection

print("Projection:\n", P)


"""
CREATE PROJECTED MESH
"""
mesh_01 = Mesh.from_shape(box)
projected_mesh = mesh_01

try:
    projected_mesh.transform(P)
except:
    print("Something went wrong with the projection")

"""
ARTISTS
"""
artist_01 = BoxArtist(box, layer = 'box')
artist_02 = MeshArtist(mesh_01, layer = 'box::projection edges')

artist_01.clear_layer()
artist_02.clear_layer()

artist_01.draw()
artist_02.draw_edges(color="#00ff00")

