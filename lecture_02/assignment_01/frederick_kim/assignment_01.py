from compas.geometry import Box
from compas.geometry import Frame
from compas.geometry import Projection
from compas.geometry import Plane
from compas_rhino.artists import BoxArtist
from compas_rhino.artists import MeshArtist
from compas.datastructures import Mesh

# Define a Frame, which is not in the origin and a bit tilted to the world frame
frame = Frame([4, 4, 4], [.5, 1, 2], [0, 1, 2])

# Create a Box with that frame
width, length, height = 1, 1, 1
box = Box(frame, width, length, height)

# Create a Projection (can be orthogonal, parallel or perspective)
point = [0,0,0]
normal = [0,0,1]
plane = Plane(point, normal)
direction = [1,1,1]
P = Projection.from_plane_and_direction(plane, direction)

# Create a Mesh from the Box
mesh = Mesh.from_shape(box)

# Apply the Projection onto the mesh
mesh_projected = mesh.transformed(P)

# Create artists
artist1 = BoxArtist(box)
artist2 = MeshArtist(mesh_projected)

# Draw
artist1.draw()
artist2.draw_edges(color="#00ff00")




