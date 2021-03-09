"""Assignment 01: Project box to xy-plane
"""
from compas.geometry import Box
from compas.geometry import Frame, Plane
from compas.geometry import Projection
from compas_rhino.artists import BoxArtist
from compas_rhino.artists import MeshArtist
from compas.datastructures import Mesh

# Define a Frame, which is not in the origin and a bit tilted to the world frame
frame = Frame.from_euler_angles([0.5, 1., 0.2])

# Create a Box with that frame
width, length, height = 1, 1, 1
box = Box(frame, width, length, height)

# Create a Projection (can be orthogonal, parallel or perspective)
point = [0, 0, 0]
normal = [0, 0, 1]
plane = Plane(point, normal)
# An orthogonal projection transformation
P = Projection.from_plane(plane)

# Create a Mesh from the Box
mesh = Mesh.from_shape(box)

# Apply the Projection onto the mesh
mesh_projected = Mesh.transformed(mesh, P)

# Create artists
artist1 = BoxArtist(box)
artist2 = MeshArtist(mesh_projected)

# Draw
artist1.draw()
artist2.draw_edges(color="#00ff00")
