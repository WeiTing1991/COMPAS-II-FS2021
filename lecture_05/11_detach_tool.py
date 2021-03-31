import os
import time

from compas_fab.backends import RosClient
from compas_fab.robots import PlanningScene
from compas_fab.robots import Tool

from compas.datastructures import Mesh
from compas.geometry import Frame

HERE = os.path.dirname(__file__)

# create tool from mesh and frame
mesh = Mesh.from_stl(os.path.join(HERE, 'vacuum_gripper.stl'))
frame = Frame([0.07, 0, 0], [0, 0, 1], [0, 1, 0])
tool = Tool(mesh, frame)

with RosClient('localhost') as client:
    robot = client.load_robot()
    scene = PlanningScene(robot)

    # Attach the tool
    robot.attach_tool(tool)
    scene.add_attached_tool()

    time.sleep(1)

    # Remove the tool
    scene.remove_attached_tool()
    scene.remove_collision_mesh('attached_tool_link_collision_0')
    robot.detach_tool()
    time.sleep(1)
