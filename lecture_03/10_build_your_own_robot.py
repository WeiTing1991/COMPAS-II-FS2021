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

# create cylinder in yz plane
radius, length = 0.3, 5
cylinder = Cylinder(Circle(Plane([0, 0, 0], [1, 0, 0]), radius), length)
cylinder.transform(Translation.from_vector([length / 2., 0, 0]))

# create robot
model = RobotModel("robot", links=[], joints=[])

# add first link to robot
link0 = model.add_link("world")

# add second link to robot
mesh = Mesh.from_shape(cylinder)
link1 = model.add_link("link1", visual_mesh=mesh, visual_color=(0.2, 0.5, 0.6))

# add the joint between the links
axis = (0, 0, 1)
origin = Frame.worldXY()
model.add_joint("joint1", Joint.CONTINUOUS, link0, link1, origin, axis)

# add another link
mesh = Mesh.from_shape(cylinder)  # create a copy!
link2 = model.add_link("link2", visual_mesh=mesh, visual_color=(0.5, 0.6, 0.2))

# add another joint to 'glue' the link to the chain
origin = Frame((length, 0, 0), (1, 0, 0), (0, 1, 0))
model.add_joint("joint2", Joint.CONTINUOUS, link1, link2, origin, axis)

# Create a configuration object matching the number of joints in your model
# configuration = ....

# Update the model using the artist
artist = RobotModelArtist(model)
# artist.update ...

# Render everything
artist.draw_visual()
artist.redraw()
