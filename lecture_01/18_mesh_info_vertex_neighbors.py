import compas
from compas.datastructures import Mesh
from compas_plotters import MeshPlotter

mesh = Mesh.from_obj(compas.get('faces.obj'))

vertex = mesh.get_any_vertex()
nbrs = mesh.vertex_neighbors(vertex)

vertexcolor = {}
vertexcolor[vertex] = (255, 0, 0)
edgecolor = {}
for nbr in nbrs:
    vertexcolor[nbr] = (0, 0, 255)
    edgecolor[vertex, nbr] = (0, 255, 0)
    edgecolor[nbr, vertex] = (0, 255, 0)

plotter = MeshPlotter(mesh, figsize=(12, 7.5))
plotter.draw_vertices(facecolor=vertexcolor)
plotter.draw_faces()
plotter.draw_edges(keys=list(edgecolor), width={edge: 2.0 for edge in edgecolor}, color=edgecolor)
plotter.show()
