
from compas_fab.robots import Configuration
from compas_rhino.artists import RobotModelArtist
import math
from compas.datastructures import Mesh
from compas.geometry import Circle
from compas.geometry import Cylinder
from compas.geometry import Sphere
from compas.geometry import Frame
from compas.geometry import Plane
from compas.geometry import Point
from compas.geometry import Translation
from compas.robots import Joint
from compas.robots import RobotModel
from compas_fab.robots import Robot

# create cylinders, spheres in yz plane
radius, length = 0.3, 5
cylinder = Cylinder(Circle(Plane([0, 0, 0], [1, 0, 0]), radius), length)
cylinder.transform(Translation.from_vector([length / 2., 0, 0]))



# create robot
model = RobotModel("robot", links=[], joints=[])



# add links and joints to the robot model

link1 = model.add_link("world")


axis = (0, 0, 1)
origin = Frame.worldXY()

# add another link
mesh2 = Mesh.from_shape(cylinder)  # create a copy!
link2 = model.add_link("link2", visual_mesh=mesh2, visual_color=(0.5, 0.6, 0.2))

# add another joint to 'glue' the link to the chain
origin = Frame((length, 0, 0), (1, 0, 0), (0, 1, 0))
model.add_joint("joint2", Joint.CONTINUOUS, link1, link2, origin, axis)

# add another link
mesh3 = Mesh.from_shape(cylinder)  # create a copy!
link3 = model.add_link("link3", visual_mesh=mesh2, visual_color=(0.5, 0.6, 0.2))

# add another joint to 'glue' the link to the chain
origin = Frame((length, 0, 0), (1, 0, 0), (0, 1, 0))
model.add_joint("joint3", Joint.CONTINUOUS, link2, link3, origin, axis)

# add another link
mesh4 = Mesh.from_shape(cylinder)  # create a copy!
link4 = model.add_link("link4", visual_mesh=mesh2, visual_color=(0.3, 0.9, 0.2))

# add another joint to 'glue' the link to the chain
origin = Frame((length, 0, 0), (1, 0, 0), (0, 1, 0))
model.add_joint("joint4", Joint.CONTINUOUS, link2, link4, origin, axis)

# add another link
mesh5 = Mesh.from_shape(cylinder)  # create a copy!
link5 = model.add_link("link5", visual_mesh=mesh2, visual_color=(0.3, 0.9, 0.2))

# add another joint to 'glue' the link to the chain
origin = Frame((length, 0, 0), (1, 0, 0), (0, 1, 0))
model.add_joint("joint5", Joint.CONTINUOUS, link3, link5, origin, axis)


#Create a configuration object matching the number of joints in your model
configuration = Configuration([0, 0,-math.pi/2,-math.pi/2,0], [Joint.CONTINUOUS, Joint.CONTINUOUS, Joint.CONTINUOUS, Joint.CONTINUOUS, Joint.CONTINUOUS])

# Update the model using the artist
artist = RobotModelArtist(model)

robot = Robot(model, artist=artist)
robot.update(configuration)

# Render everything
artist.draw_visual()
artist.redraw()
