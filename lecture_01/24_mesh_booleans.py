from compas.datastructures import Mesh
from compas.geometry import Box
from compas.geometry import Frame
from compas.geometry import boolean_union_mesh_mesh

b1 = Box(Frame([+4, +4, 0], [1, 0, 0], [0, 1, 0]), 10, 10, 10)
b2 = Box(Frame([-4, -4, 0], [1, 0, 0], [0, 1, 0]), 10, 10, 10)

A = Mesh.from_shape(b1)
B = Mesh.from_shape(b2)

A.quads_to_triangles()
B.quads_to_triangles()

A = A.to_vertices_and_faces()
B = B.to_vertices_and_faces()

# Use best boolean union available depending on context
V, F = boolean_union_mesh_mesh(A, B)

mesh = Mesh.from_vertices_and_faces(V, F)
print(mesh.summary())
