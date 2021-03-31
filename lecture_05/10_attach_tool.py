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

    # now we can convert frames at robot's tool tip and flange
    frames_tcf = [Frame((-0.309, -0.046, -0.266), (0.276, 0.926, -0.256), (0.879, -0.136, 0.456))]
    frames_tcf0 = robot.from_tcf_to_t0cf(frames_tcf)

    time.sleep(1)
