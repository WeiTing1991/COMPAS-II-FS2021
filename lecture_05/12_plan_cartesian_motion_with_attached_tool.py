import os

from compas_fab.backends import RosClient
from compas_fab.robots import Configuration
from compas_fab.robots import Tool

from compas.datastructures import Mesh
from compas.geometry import Frame

HERE = os.path.dirname(__file__)

# create tool from mesh and frame
mesh = Mesh.from_stl(os.path.join(HERE, 'vacuum_gripper.stl'))
frame = Frame([0.07, 0, 0], [0, 0, 1], [0, 1, 0])
tool = Tool(mesh, frame)

element_height = 0.014
approach_distance = 0.05

with RosClient('localhost') as client:
    robot = client.load_robot()

    # 1. Set tool
    robot.attach_tool(tool)

    # 2. Define start configuration
    start_configuration = Configuration.from_revolute_values([-5.961, 4.407, -2.265, 5.712, 1.571, -2.820])

    # 3. Define frames
    picking_frame = Frame([-0.43, 0, element_height], [1, 0, 0], [0, 1, 0])
    approach_picking_frame = Frame([-0.43, 0, element_height + approach_distance], [1, 0, 0], [0, 1, 0])
    frames = [picking_frame, approach_picking_frame]

    # 4. Convert frames to tool0_frames
    frames_tool0 = robot.from_tcf_to_t0cf(frames)

    trajectory = robot.plan_cartesian_motion(frames_tool0,
                                             start_configuration,
                                             options=dict(max_step=0.01))

    print("Computed cartesian path with %d configurations, " % len(trajectory.points))
    print("following %d%% of requested trajectory." % (trajectory.fraction * 100))
    print("Executing this path at full speed would take approx. %.3f seconds." % trajectory.time_from_start)
