"""Assignment 03: Using inverse kinematics
"""
import json
import os
import compas_fab
from compas_fab.backends import RosClient
from compas_fab.robots import Configuration
from compas_fab.utilities import write_data_to_json, read_data_from_json
from compas.geometry import Frame
from compas.geometry import Point
from compas.geometry import Vector


# This function defines the inputs of your assignment, you get a compas_fab.robots.Robot and a Frame
# and are expected to return ONE valid configuration to reach that frame
def calculate_ik(robot, frame):
    # 1. define a valid start configuration for your frames
    start_configuration = robot.zero_configuration()
    # 2. use inverse kinematics to find out a valid configuration
    configuration = robot.inverse_kinematics(frame, start_configuration)
    return configuration

def store_configurations(configurations):
    # 3. store all found configurations in a JSON file

    # define filepath and filename
    filename = "assignment_03.json"
    directory = "C:/Users/trtku/OneDrive/Data/03_MAS/01_github/compas_fs2021/compas_2_local/lecture_04/ko_tsuruta"
    filepath = os.path.join(directory, filename)

    # translate configurations into json serialisable structure
    serial_configs = [config.to_data() for config in configurations]

    # export json
    write_data_to_json(serial_configs, filepath)

def configuration_from_json():
    # define filepath
    filename = "assignment_03.json"
    directory = "C:/Users/trtku/OneDrive/Data/03_MAS/01_github/compas_fs2021/compas_2_local/lecture_04/ko_tsuruta"
    filepath = os.path.join(directory, filename)

    # translate json into deserialisable data
    desirial_data = read_data_from_json(filepath)

    # get configurations from json
    desirial_configs = [Configuration.from_data(data) for data in desirial_data]

    return desirial_configs


# RUN code
command_line = False # toggle off to run in GH

if command_line:
    # Use the following to test from the command line
    # Or copy solution_viewer.ghx next to the folder where you created assignment_03.py to visualize the same in Grasshopper
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

            # And call our assignment functions for each frame in the example
            configurations = []
            for frame in frame_list:
                configuration = calculate_ik(robot, frame)
                configurations.append(configuration)
                print("Found configuration", configuration)

            store_configurations(configurations)


    # import json check from the command line
    configurations = configuration_from_json()
    print("-----reading json-----")
    for config in configurations:
        print("Found configuration", config)
