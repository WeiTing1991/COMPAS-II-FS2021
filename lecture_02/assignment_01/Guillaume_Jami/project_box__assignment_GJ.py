"""
    Assignment 01: Project box to xy-plane
    Guillaume Jami 07.03.2021

"""
from compas.geometry import Box
from compas.geometry import Frame, Plane
from compas.geometry import Vector
from compas.geometry import Projection
from compas_rhino.artists import BoxArtist
from compas_rhino.artists import FrameArtist
from compas_rhino.artists import MeshArtist
from compas.datastructures import Mesh
from compas.geometry import Transformation

# Define a Frame, which is not in the origin and a bit tilted to the world frame

frame = Frame([1, 0, 0], [0, 1, 0], [1, 0, 0])
frame1 = Frame([2, 2, 2], [0.978, 0.010, -0.210], [0.090, 0.882, 0.463])

# Create a Box with that frame
width, length, height = 1, 1, 1
box = Box(frame, width, length, height)

box_frame_transformed = frame1.to_world_coordinates(box.frame)
box_transformed = Box(box_frame_transformed, width, length, height)

# Create a Projection (can be orthogonal, parallel or perspective)
point = [0, 0, 0]
normal = [0, 0, -1]
plane = Plane(point, normal)
direction = [2, -2, 1]
P = Projection.from_plane_and_direction(plane, direction)

# Create a Mesh from the Box
mesh = Mesh.from_shape(box)
tmesh = Mesh.from_shape(box_transformed)

# Apply the Projection onto the mesh
mesh_projected = tmesh.transformed(P)

# clear layer
artist = BoxArtist(box, layer="Default")
artist.clear_layer()

# defining Artists
artist1 = BoxArtist(box)
artist2 = BoxArtist(box_transformed)
artist3 = MeshArtist(mesh_projected)
artist4 = FrameArtist(frame, scale=1.0)
artist5 = FrameArtist(frame1, scale=1.0)

# Draw
artist1.draw()
artist2.draw()
artist3.draw_edges(color="#00ffff")
artist4.draw()
artist5.draw()
