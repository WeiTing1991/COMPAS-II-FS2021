import os
import compas

from compas.robots import LocalPackageMeshLoader
from compas.robots import RobotModel

# Set high precision to import meshes defined in meters
compas.PRECISION = '12f'
models_path = os.path.join(os.path.dirname(__file__), 'models')

# Prepare loader
loader = LocalPackageMeshLoader(models_path, 'ur_description')

# Create robot model from URDF
model = RobotModel.from_urdf_file(loader.load_urdf('ur5.urdf'))

# Load geometry
model.load_geometry(loader)

print(model)
