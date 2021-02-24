import compas
from compas.datastructures import Mesh
from compas_plotters import MeshPlotter

mesh = Mesh.from_obj(compas.get('faces.obj'))

plotter = MeshPlotter(mesh, figsize=(12, 7.5))
plotter.draw_vertices(
    facecolor={vertex: (255, 0, 0) for vertex in mesh.vertices_on_boundary()},
)
plotter.draw_faces()
plotter.show()
