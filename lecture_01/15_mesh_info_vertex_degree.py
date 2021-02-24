import compas
from compas.datastructures import Mesh
from compas_plotters import MeshPlotter

mesh = Mesh.from_obj(compas.get('faces.obj'))

plotter = MeshPlotter(mesh, figsize=(12, 7.5))
plotter.draw_vertices(text={vertex: str(mesh.vertex_degree(vertex)) for vertex in mesh.vertices()}, radius=0.2)
plotter.draw_faces()
plotter.show()
