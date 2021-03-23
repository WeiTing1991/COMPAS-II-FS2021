import os
import json
from compas_fab.backends import RosClient
from compas_fab.robots import Configuration
from compas_fab.utilities import write_data_to_json

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
    HERE = os.path.dirname(__file__)
    FILE1 = os.path.join(HERE, 'IK_config_data.json')
    config_data_list = []
    for config in configurations:
        config_data_list.append(config.data)  
    write_data_to_json(config_data_list, FILE1) 

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