from compas_rhino.artists import RobotModelArtist

from compas.robots import LocalPackageMeshLoader
from compas.robots import RobotModel

model = RobotModel.from_urdf_file('models/05_origins_meshes.urdf')

loader = LocalPackageMeshLoader('models', 'basic')
model.load_geometry(loader)

artist = RobotModelArtist(model, layer='COMPAS::Robot Viz')
artist.clear_layer()
artist.draw_visual()
