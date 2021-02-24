# Blender
import compas
from compas.datastructures import Mesh
from compas_blender.artists import MeshArtist

mesh = Mesh.from_obj(compas.get('hypar.obj'))

artist = MeshArtist(mesh)
artist.draw_mesh()
