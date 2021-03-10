from compas.geometry import Frame
from compas.robots import LocalPackageMeshLoader
from compas.robots import RobotModel
from compas_rhino.artists import RobotModelArtist

from ur_kinematics import inverse_kinematics_ur5

loader = LocalPackageMeshLoader('models', 'ur_description')
model = RobotModel.from_urdf_file(loader.load_urdf('ur5.urdf'))
model.load_geometry(loader)

f = Frame((0.417, 0.191, -0.005), (-0.000, 1.000, 0.000), (1.000, 0.000, 0.000))
f.point /= 0.001

sols = inverse_kinematics_ur5(f)

artist = RobotModelArtist(model, layer='COMPAS::Robot Viz')
artist.clear_layer()

for joint_values in sols:
    # Create joint state dictionary
    joint_names = model.get_configurable_joint_names()
    joint_state = dict(zip(joint_names, joint_values))
    artist.update(joint_state)
    artist.draw_visual()
