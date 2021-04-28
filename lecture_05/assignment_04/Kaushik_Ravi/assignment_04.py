"""Assignment 03: Using inverse kinematics
"""
import json
import os
import compas
from compas_fab.backends import RosClient
from compas_fab.robots import Configuration
from compas.utilities import DataEncoder

from compas.geometry import Frame
from compas.geometry import Point
from compas.geometry import Vector

HERE = os.path.dirname(__file__)
FILE = os.path.join(HERE, 'robot.json')


def store_configurations(configurations):
    compas.json_dump(configurations,'data.json')