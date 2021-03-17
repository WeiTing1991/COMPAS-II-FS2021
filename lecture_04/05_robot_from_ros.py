# Before running this example, make sure to run
# "docker compose up" on the docker/moveit folder
from compas_fab.backends import RosClient

# Load robot without geometry
with RosClient('localhost') as ros:
    robot = ros.load_robot(load_geometry=False)
    # robot already contains model, semantics and client
    robot.info()
