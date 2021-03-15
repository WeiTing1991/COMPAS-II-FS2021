# * Create a box at a certain location with a certain orientation.
# * Create a Projection (can be orthogonal, parallel or perspective)
# * Convert the box to a mesh and project the it onto the xy-plane.
# * Use artists to draw the result

"""Assignment 01: Project box to xy-plane
"""
from compas.geometry import Point, Box, Frame, Plane
from compas.geometry import Projection, matrix_from_parallel_projection
from compas_rhino.artists import BoxArtist
from compas_rhino.artists import MeshArtist
from compas_rhino.artists import FrameArtist, PlaneArtist
from compas.datastructures import Mesh

# Define a Frame, which is not in the origin and a bit tilted to the world frame
frame = Frame.from_plane(Plane([20, 40, 60], [0, 1, 1]))
p = Plane(Point(0, 0, 0), [0, 0, 1])
d = 1, 0, 1

# Create a Box with that frame
box = Box(frame, 10, 15, 20)

# Create a Projection (can be orthogonal, parallel or perspective)
P = Projection.from_plane_and_direction(p, d)
# P = matrix_from_parallel_projection(p, d)

# Create a Mesh from the Box
mesh = Mesh.from_shape(box)

## Apply the Projection onto the mesh
mesh_projected = mesh.transformed(P)

# Create artists
artist1 = BoxArtist(box)
artist2 = MeshArtist(mesh_projected)
artist3 = FrameArtist(frame)

# Draw
artist1.draw()
artist2.draw_edges(color="#00ff00")
artist3.draw()
