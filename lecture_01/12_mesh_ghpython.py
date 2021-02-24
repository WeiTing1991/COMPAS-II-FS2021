# Ghpython
import compas
from compas.datastructures import Mesh
from compas_ghpython.artists import MeshArtist

mesh = Mesh.from_obj(compas.get('hypar.obj'))

artist = MeshArtist(mesh)
a = artist.draw()
