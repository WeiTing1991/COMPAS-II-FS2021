import os

from compas.robots import LocalPackageMeshLoader
from compas.robots import RobotModel

models_path = os.path.join(os.path.dirname(__file__), 'models')
loader = LocalPackageMeshLoader(models_path, 'ur_description')
model = RobotModel.from_urdf_file(loader.load_urdf('ur5.urdf'))

# Get some relevant link names for FK
print(model.get_base_link_name())
print(model.get_end_effector_link_name())

# Create joint state dictionary
joint_names = model.get_configurable_joint_names()
joint_values = [0.] * 6
joint_state = dict(zip(joint_names, joint_values))
# can also use this for joint state:
# joint_state = {'shoulder_pan_joint': 0, 'shoulder_lift_joint':0, 'elbow_joint': 0, 'wrist_1_joint': 0, 'wrist_2_joint':0, 'wrist_3_joint': 0}

# Get FK for tip
print (model.forward_kinematics(joint_state))
# Get FK for base
print (model.forward_kinematics(joint_state, link_name=model.get_base_link_name()))
