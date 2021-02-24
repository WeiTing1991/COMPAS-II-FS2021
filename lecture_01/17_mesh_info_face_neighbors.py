import compas
from compas.datastructures import Mesh
from compas_plotters import MeshPlotter

mesh = Mesh.from_obj(compas.get('faces.obj'))

face = mesh.get_any_face()
nbrs = mesh.face_neighbors(face)

facecolor = {}
facecolor[face] = (255, 200, 200)
for nbr in nbrs:
    facecolor[nbr] = (200, 255, 200)

plotter = MeshPlotter(mesh, figsize=(12, 7.5))
plotter.draw_vertices()
plotter.draw_faces(
    text={face: str(mesh.face_degree(face)) for face in mesh.faces()},
    facecolor=facecolor
)
plotter.show()
