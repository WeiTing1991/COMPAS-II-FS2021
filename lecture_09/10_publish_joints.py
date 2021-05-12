# This script is meant to be run by the course lead from the real robot cell
# If you want to run this on your own computer using ABB RobotStudio simulation
# you will need to install the `requests` package: conda install requests
import json
import math
import time

import requests
import requests.auth
import roslibpy
from compas.robots import Joint
from compas_fab.backends import RosClient
from compas_fab.backends.ros import JointState
from helpers import Rate

if __name__ == '__main__':
    session = requests.Session()
    session.auth = requests.auth.HTTPDigestAuth('Default User', 'robotics')

    url = 'http://localhost/rw/motionsystem/mechunits/ROB_1/jointtarget?json=1'

    with RosClient() as ros:
        topic = roslibpy.Topic(ros, '/joint_states', 'sensor_msgs/JointState')
        topic.advertise()

        rate = Rate(10)
        types = dict(joint1=Joint.REVOLUTE, joint2=Joint.REVOLUTE, joint3=Joint.PRISMATIC, joint4=Joint.REVOLUTE)

        while True:
            response = session.get(url)
            joints = json.loads(response.text)
            joints = joints['_embedded']['_state'][0]

            joint_state = JointState()
            for j in range(4):
                name = 'joint{}'.format(j + 1)
                position = float(joints['rax_{}'.format(j + 1)])
                jtype = types[name]

                # Convert units from RRC to ROS
                if jtype == Joint.REVOLUTE:
                    position = math.radians(position)
                if jtype == Joint.PRISMATIC:
                    position = position / 1000.

                joint_state.name.append(name)
                joint_state.position.append(position)

            topic.publish(joint_state.msg)

            print('{} | {} {} {} {}\r'.format(time.time(), joints['rax_1'], joints['rax_2'], joints['rax_3'], joints['rax_4']), end='', flush=True)
            rate.sleep()
