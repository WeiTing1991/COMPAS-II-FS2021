"""Assignment 01: Project box to xy-plane
"""
from compas.geometry import Box
from compas.geometry import Point
from compas.geometry import Vector
from compas.geometry import Frame
from compas.geometry import Projection
from compas.geometry import Plane
from compas_rhino.artists import BoxArtist
from compas_rhino.artists import FrameArtist
from compas_rhino.artists import MeshArtist
from compas_rhino.artists import PlaneArtist # not implemented

from compas.datastructures import Mesh

# Define a Frame, which is not in the origin and a bit tilted to the world frame
frame = Frame(Point(1, 1, 3), Vector(1, 0, 1), Vector(0, 1, 1))

# Create a Box with that frame
box = Box(frame, 2, 3, 6)

# create a plane for the projection
planexy = Plane.worldXY()

# Create a Projection (can be orthogonal, parallel or perspective)
P3 = Projection.from_plane(planexy)  # orthogonal Projection to project onto a plane
P4 = Projection.from_plane_and_direction(planexy, direction=Vector(-2, 2, 1))  # parallel projection
P5 = Projection.from_plane_and_point(planexy, Point(3, -3, -1))  # perspective Projection

# Create a Mesh from the Box
mesh = Mesh.from_shape(box)

# Apply the Projection onto the mesh
mesh_projected3 = mesh.transformed(P3)
mesh_projected4 = mesh.transformed(P4)
mesh_projected5 = mesh.transformed(P5)

# Create artists
artist1 = BoxArtist(box)
artist2 = FrameArtist(frame)
artist3 = MeshArtist(mesh_projected3, layer="P3")
artist4 = MeshArtist(mesh_projected4, layer="P4")
artist5 = MeshArtist(mesh_projected5, layer="P5")

#clear layers
artistl = [artist1, artist2, artist3, artist4, artist5]
for arty in artistl:
    arty.clear_layer()

# Draw
artist1.draw()
artist2.draw()
artist3.draw_edges(color="#00ffa0")
artist4.draw_edges(color=(200, 0, 0))
artist5.draw_edges(color=(200, 100, 0))
