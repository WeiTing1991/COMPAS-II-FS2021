# Units:
#  - Revolute joint : radiants
#  - Prismatic joint: meters

import math
from compas.robots.model import Joint
from compas_fab.robots import Configuration

print('Default constructor')
print (Configuration([math.pi, 4], [Joint.REVOLUTE, Joint.PRISMATIC]))
print (Configuration([math.pi, 4], [Joint.REVOLUTE, Joint.PRISMATIC], ['joint_1', 'ext_axis_1']))

print()
print('Construct from revolute values')
print (Configuration.from_revolute_values([math.pi, 0]))
print (Configuration.from_revolute_values([math.pi, 0], ['joint_1', 'joint_2']))

print()
print('Construct from prismatic & revolute values')
print (Configuration.from_prismatic_and_revolute_values([4], [math.pi]))
print (Configuration.from_prismatic_and_revolute_values([4], [math.pi], ['ext_axis_1', 'joint_1']))

print()
print('Merge two configurations')
ext_axes = Configuration([4], [Joint.PRISMATIC], ['ext_axis_1'])
arm_joints = Configuration([math.pi], [Joint.REVOLUTE], ['joint_1'])
full_cfg = ext_axes.merged(arm_joints)
print(full_cfg)
