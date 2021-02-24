import compas
from compas.datastructures import Mesh
from compas_rhino.artists import MeshArtist

mesh = Mesh.from_obj(compas.get('tubemesh.obj'))

artist = MeshArtist(mesh, layer='Tubemesh')
artist.clear_layer()
artist.draw()
artist.draw_vertexnormals()
