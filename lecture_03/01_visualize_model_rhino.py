from compas_rhino.artists import RobotModelArtist

from compas.robots import RobotModel

model = RobotModel.from_urdf_file('models/01_myfirst.urdf')

artist = RobotModelArtist(model, layer='COMPAS::Robot Viz')
artist.clear_layer()
artist.draw_visual()
