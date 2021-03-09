# Before running this example, make sure to run
# "docker compose up" on the docker folder
import compas
from compas_fab.backends import RosClient

# Set high precision to import meshes defined in meters
compas.PRECISION = '12f'

# Load robot and its geometry
with RosClient('localhost') as ros:
    robot = ros.load_robot(load_geometry=True)
    # robot already contains model, semantics and client
    robot.info()
