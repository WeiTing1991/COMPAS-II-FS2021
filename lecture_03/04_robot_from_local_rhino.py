import compas
from compas.robots import LocalPackageMeshLoader
from compas.robots import RobotModel
from compas_rhino.artists import RobotModelArtist

# Set high precision to import meshes defined in meters
compas.PRECISION = '12f'

# Prepare loader
loader = LocalPackageMeshLoader('models', 'ur_description')

# Create robot model from URDF
model = RobotModel.from_urdf_file(loader.load_urdf('ur5.urdf'))

# Load geometry
model.load_geometry(loader)

# Draw model
artist = RobotModelArtist(model, layer='COMPAS::Robot Viz')
artist.clear_layer()
artist.draw_visual()
