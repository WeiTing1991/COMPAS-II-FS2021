import os
from compas.geometry import Frame
from compas.robots import LocalPackageMeshLoader
from compas.robots import RobotModel
from compas_fab.robots import Configuration

from ur_kinematics import inverse_kinematics_ur5

models_path = os.path.join(os.path.dirname(__file__), 'models')
loader = LocalPackageMeshLoader(models_path, 'ur_description')
model = RobotModel.from_urdf_file(loader.load_urdf('ur5.urdf'))

f = Frame((0.417, 0.191, -0.005), (-0.000, 1.000, 0.000), (1.000, 0.000, 0.000))
f.point /= 0.001

sols = inverse_kinematics_ur5(f)

for joint_values in sols:
    joint_names = model.get_configurable_joint_names()
    print(Configuration.from_revolute_values(joint_values, joint_names))
