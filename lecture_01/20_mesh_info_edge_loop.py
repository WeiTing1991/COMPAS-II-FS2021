import random
import compas
from compas.datastructures import Mesh
from compas_plotters import MeshPlotter

mesh = Mesh.from_obj(compas.get('quadmesh.obj'))

start = random.choice(list(mesh.edges()))
edges = mesh.edge_loop(start)

edgecolor = {}
for edge in edges:
    edgecolor[edge] = (0, 255, 0)

edgecolor[start] = (255, 0, 0)

plotter = MeshPlotter(mesh, figsize=(12, 7.5))
plotter.draw_vertices(radius=0.03)
plotter.draw_faces()
plotter.draw_edges(keys=edges, color=edgecolor, width=2.0)
plotter.show()
