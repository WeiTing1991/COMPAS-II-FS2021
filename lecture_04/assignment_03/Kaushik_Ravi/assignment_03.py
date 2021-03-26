"""Assignment 03: Using inverse kinematics
"""
import json
import os
from compas_fab.backends import RosClient
from compas_fab.robots import Configuration
from compas.utilities import DataEncoder

from compas.geometry import Frame
from compas.geometry import Point
from compas.geometry import Vector

HERE = os.path.dirname(__file__)
FILE = os.path.join(HERE, 'robot.json')

def calculate_ik(robot, frame):
    start_configuration = robot.zero_configuration()
    configuration = robot.inverse_kinematics(frame, start_configuration)
    return configuration

def store_configurations(configurations):
    with open(FILE, 'w') as f:
        json.dump(configurations, f, cls=DataEncoder)
    pass

if __name__ == '__main__':
    frame_list = [
        Frame(Point(0.084, 0.319, 0.175), Vector(0.000, 0.000, -1.000), Vector(0.000, 1.000, 0.000)),
        Frame(Point(0.152, 0.317, 0.175), Vector(0.000, 0.000, -1.000), Vector(0.000, 1.000, 0.000)),
        Frame(Point(0.220, 0.315, 0.175), Vector(0.000, 0.000, -1.000), Vector(0.000, 1.000, 0.000)),
        Frame(Point(0.288, 0.313, 0.175), Vector(0.000, 0.000, -1.000), Vector(0.000, 1.000, 0.000)),
        Frame(Point(0.357, 0.310, 0.175), Vector(0.000, 0.000, -1.000), Vector(0.000, 1.000, 0.000)),
        Frame(Point(0.425, 0.308, 0.175), Vector(0.000, 0.000, -1.000), Vector(0.000, 1.000, 0.000)),
        Frame(Point(0.493, 0.306, 0.175), Vector(0.000, 0.000, -1.000), Vector(0.000, 1.000, 0.000)),
        Frame(Point(0.561, 0.303, 0.175), Vector(0.000, 0.000, -1.000), Vector(0.000, 1.000, 0.000)),
        Frame(Point(0.629, 0.301, 0.175), Vector(0.000, 0.000, -1.000), Vector(0.000, 1.000, 0.000)),
        Frame(Point(0.698, 0.299, 0.175), Vector(0.000, 0.000, -1.000), Vector(0.000, 1.000, 0.000)),
        Frame(Point(0.766, 0.297, 0.175), Vector(0.000, 0.000, -1.000), Vector(0.000, 1.000, 0.000))
    ]

    # Loads the robot from ROS
    with RosClient('localhost') as client:
        robot = client.load_robot()
        configurations = []
        for frame in frame_list:
            start_configuration = robot.zero_configuration()
            configuration = robot.inverse_kinematics(frame, start_configuration)
            configurations.append(configuration)
            print("Found configuration", configuration)

        store_configurations(configurations)
