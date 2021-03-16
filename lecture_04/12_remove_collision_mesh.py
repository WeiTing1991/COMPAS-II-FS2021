import time

from compas_fab.backends import RosClient
from compas_fab.robots import PlanningScene

with RosClient('localhost') as client:
    robot = client.load_robot()
    scene = PlanningScene(robot)
    scene.remove_collision_mesh('brick_wall')
    scene.remove_collision_mesh('floor')

    # sleep a bit before terminating the client
    time.sleep(1)
