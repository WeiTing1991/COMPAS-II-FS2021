# Before running this example, make sure to run
# "docker compose up" on the docker/moveit folder
import compas
from compas_fab.backends import RosClient
from compas_rhino.artists import RobotModelArtist

# Set high precision to import meshes defined in meters
compas.PRECISION = '12f'

# Load robot and its geometry
with RosClient('localhost') as ros:
    robot = ros.load_robot(load_geometry=True)
    robot.artist = RobotModelArtist(robot.model, layer='COMPAS::Robot Viz')

robot.artist.clear_layer()
robot.artist.draw()
