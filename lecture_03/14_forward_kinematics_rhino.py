from compas.robots import LocalPackageMeshLoader
from compas.robots import RobotModel
from compas_rhino.artists import FrameArtist
from compas_rhino.artists import RobotModelArtist

loader = LocalPackageMeshLoader('models', 'ur_description')
model = RobotModel.from_urdf_file(loader.load_urdf('ur5.urdf'))
model.load_geometry(loader)

joints = dict(shoulder_pan_joint=0, shoulder_lift_joint=0, elbow_joint=0,
              wrist_1_joint=0, wrist_2_joint=0, wrist_3_joint=0)

frame = model.forward_kinematics(joints)

artist = FrameArtist(frame, layer='COMPAS::Robot Viz')
artist.clear_layer()
artist.draw()

artist = RobotModelArtist(model, layer='COMPAS::Robot Viz')
artist.update(joints)
artist.draw_visual()
