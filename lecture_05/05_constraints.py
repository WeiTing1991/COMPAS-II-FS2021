import math
from compas.geometry import Frame
from compas_fab.backends import RosClient
from compas_fab.robots import Configuration

with RosClient('localhost') as client:
    robot = client.load_robot()
    group = robot.main_group_name

    frame = Frame([0.4, 0.3, 0.4], [0, 1, 0], [0, 0, 1])
    tolerance_position = 0.001
    tolerance_axes = [math.radians(1)] * 3

    # create goal constraints from frame
    goal_constraints = robot.constraints_from_frame(frame,
                                                    tolerance_position,
                                                    tolerance_axes,
                                                    group)
    print(goal_constraints)
