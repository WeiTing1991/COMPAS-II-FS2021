"""
   Assignment 02: Build your own robot model
   Guillaume Jami
"""
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
import math as m

# create cylinder in xy plane

radius = 0.3
length, length1 = 10, 5 
cylinder = Cylinder(Circle(Plane([0, 0, 0], [0, 0, 1]), radius), length)
cylinder1 = Cylinder(Circle(Plane([0, 0, 0], [0, 0, 1]), radius), length1)
cylinder.transform(Translation.from_vector([0, 0, length / 2.]))
cylinder1.transform(Translation.from_vector([0, 0, length1 / 2.]))



# create robot
model = RobotModel("robot", links=[], joints=[])

""" defines link """

# link0 = model.add_link(..)
link0 = model.add_link("world")

# link1 = model.add_link(..)
mesh = Mesh.from_shape(cylinder)
link1 = model.add_link("link1", visual_mesh=mesh, visual_color=(0.2, 0.5, 0.6))

# link2 = model.add_link(..)
mesh = Mesh.from_shape(cylinder1)  # create a copy!
link2 = model.add_link("link2", visual_mesh=mesh, visual_color=(0.5, 0.6, 0.2))

# link4 = model.add_link(..)
mesh = Mesh.from_shape(cylinder1)  # create a copy!
link3 = model.add_link("link3", visual_mesh=mesh, visual_color=(0.5, 0.6, 0.4))

# link3 = model.add_link(..)
mesh = Mesh.from_shape(cylinder1)  # create a copy!
link4 = model.add_link("link4", visual_mesh=mesh, visual_color=(0.5, 0.6, 0.7))

""" defines joints  """

# joint1
axis = (0, 1, 0)
origin = Frame((0, 0, 0), (1, 0, 0), (0, 1, 0))
joint1 = model.add_joint("joint1", Joint.CONTINUOUS, link0, link1, origin, axis)

# joint2
origin = Frame((0, 0, length), (1, 0, 0), (0, 1, 0))
joint2 = model.add_joint("joint2", Joint.CONTINUOUS, link1, link2, origin, axis)

# joint3
origin = Frame((0, 0, length1), (1, 0, 0), (0, 1, 0))
joint3 = model.add_joint("joint3", Joint.CONTINUOUS, link2, link3, origin, axis)

# joint4
origin = Frame((0, 0, length1), (1, 0, 0), (0, 1, 0))
joint4 = model.add_joint("joint4", Joint.CONTINUOUS, link3, link4, origin, axis)

# Create a configuration object matching the number of joints in your model
configuration = dict(joint1=m.radians(0), joint2=m.radians(90), joint3=m.radians(90), joint4=m.radians(90))

# Update the model using the artist
artist = RobotModelArtist(model)
artist.update(configuration)
artist.clear_layer()

# Render everything
artist.draw_visual()
artist.redraw()
