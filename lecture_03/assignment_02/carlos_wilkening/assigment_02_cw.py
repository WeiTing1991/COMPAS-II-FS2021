# Rhino
from compas_fab.robots import Configuration
from compas_rhino.artists import RobotModelArtist

from compas.datastructures import Mesh
from compas.geometry import Circle
from compas.geometry import Cylinder
from compas.geometry import Frame
from compas.geometry import Plane
from compas.geometry import Translation
from compas.robots import Joint
from compas.robots import RobotModel

# create cylinders in yz plane
radius0, length0 = 1.5, 3
cylinder0 = Cylinder(Circle(Plane([0, 0, 0], [1, 0, 0]), radius0), length0)
cylinder0.transform(Translation.from_vector([length0 / 2., 0, 0]))

radius1, length1 = 0.8, 7
cylinder1 = Cylinder(Circle(Plane([0, 0, 0], [1, 0, 0]), radius1), length1)
cylinder1.transform(Translation.from_vector([length1 / 2., 0, 0]))

radius, length = 0.6, 5
cylinder = Cylinder(Circle(Plane([0, 0, 0], [1, 0, 0]), radius), length)
cylinder.transform(Translation.from_vector([length / 2., 0, 0]))

## create robot
model = RobotModel("robot", links=[], joints=[])
#
## add first link to robot
link0 = model.add_link("world")

## link1
mesh = Mesh.from_shape(cylinder0)
link1 = model.add_link("link1", visual_mesh=mesh, visual_color=(0.7, 0.6, 0.2))
## joint1
axis = (0, 0, 1)
origin = Frame.worldXY()
model.add_joint("joint1", Joint.CONTINUOUS, link0, link1, origin, axis)


## link2
mesh = Mesh.from_shape(cylinder1)  # create a copy!
link2 = model.add_link("link2", visual_mesh=mesh, visual_color=(0.5, 0.6, 0.2))
## joint2
origin = Frame((length0, 0, 0), (1, 0, 0), (0, 1, 0))
model.add_joint("joint2", Joint.CONTINUOUS, link1, link2, origin, axis)


## link3
mesh = Mesh.from_shape(cylinder)  # create a copy!
link3 = model.add_link("link3", visual_mesh=mesh, visual_color=(0.2, 0.6, 0.2))
## joint3
origin = Frame((length1, 0, 0), (1, 0, 0), (0, 1, 0))
model.add_joint("joint3", Joint.CONTINUOUS, link2, link3, origin, axis)


## link4
mesh = Mesh.from_shape(cylinder)  # create a copy!
link4 = model.add_link("link4", visual_mesh=mesh, visual_color=(0.2, 0.5, 0.6))
## joint4
origin = Frame((length, 0, 0), (1, 0, 0), (0, 1, 0))
model.add_joint("joint4", Joint.CONTINUOUS, link3, link4, origin, axis)

## link5
mesh = Mesh.from_shape(cylinder1)  # create a copy!
link5 = model.add_link("link5", visual_mesh=mesh, visual_color=(0.2, 0.5, 0.8))
## joint5
origin = Frame((length, 0, 0), (1, 0, 0), (0, 1, 0))
model.add_joint("joint5", Joint.CONTINUOUS, link4, link5, origin, axis)

## link6
mesh = Mesh.from_shape(cylinder0)  # create a copy!
link6 = model.add_link("link6", visual_mesh=mesh, visual_color=(0.2, 0.5, 1))
## joint6
origin = Frame((length1, 0, 0), (1, 0, 0), (0, 1, 0))
model.add_joint("joint6", Joint.CONTINUOUS, link5, link6, origin, axis)
#
## Create a configuration object matching the number of joints in your model
configuration = Configuration.from_revolute_values([-0.1,-0.9,2,-2, 2,-0.9], joint_names=['joint1','joint2', 'joint3', 'joint4', 'joint5', 'joint6'])

# Update the model using the artist
artist = RobotModelArtist(model, layer = 'Compas::DIYRobot')
artist.update(configuration.joint_dict)

# Render everything
artist.draw_visual()
artist.redraw()
