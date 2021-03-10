from compas.robots import RobotModel
from compas.robots import Joint
from compas.robots import Link

model = RobotModel('ur10e',
              joints=[
                  Joint('shoulder_pan_joint', 'revolute', parent='base_link', child='shoulder_link'),
                  Joint('shoulder_lift_joint', 'revolute', parent='shoulder_link', child='upper_arm_link'),
                  Joint('elbow_joint', 'revolute', parent='upper_arm_link', child='forearm_link'),
                  Joint('wrist_1_joint', 'revolute', parent='forearm_link', child='wrist_1_link'),
                  Joint('wrist_2_joint', 'revolute', parent='wrist_1_link', child='wrist_2_link'),
                  Joint('wrist_3_joint', 'revolute', parent='wrist_2_link', child='wrist_3_link'),
              ], links=[
                  Link('base_link'),
                  Link('shoulder_link'),
                  Link('upper_arm_link'),
                  Link('forearm_link'),
                  Link('wrist_1_link'),
                  Link('wrist_2_link'),
                  Link('wrist_3_link'),
              ])
print(model)
