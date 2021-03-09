# Assignment 01

'''Project box to xy-plane:

* Create a box at a certain location with a certain orientation.
* Create a Projection (can be orthogonal, parallel or perspective)
* Convert the box to a mesh and project the it onto the xy-plane.
* Use artists to draw the result
'''

"""Assignment 01: Project box to xy-plane
"""
from compas.geometry import Box
from compas.geometry import Frame
from compas.geometry import Projection, Plane, Vector
from compas_rhino.artists import BoxArtist
from compas_rhino.artists import MeshArtist
from compas.datastructures import Mesh

# Define a Frame, which is not in the origin and a bit tilted to the world frame
frame_1 = Frame([7,7,7], [0.5, 1, 0], [1, 0, 0.5])

# Create a Box with that frame
box_1 = Box(frame_1, 1, 2, 3)

# Create a Projection transformation (can be orthogonal, parallel or perspective)
plane_1 = Plane([0,0,0], [0,0,1])
P = Projection.from_plane_and_point(plane_1, (10,10,10))

# Create a Mesh from the Box
mesh = Mesh.from_shape(box_1)

# Apply the Projection onto the mesh
mesh_projected = mesh.transformed(P)

# Create artists
artist1 = BoxArtist(box_1)
artist2 = MeshArtist(mesh_projected)

# Draw
artist1.draw()
artist2.draw_edges(color="#00ff00")

