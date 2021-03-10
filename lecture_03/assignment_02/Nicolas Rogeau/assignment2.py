# Rhino
from compas_fab.robots import Configuration
from compas_rhino.artists import RobotModelArtist
from compas_rhino.artists import CylinderArtist
from compas.datastructures import Mesh
from compas.geometry import Circle
from compas.geometry import Cylinder
from compas.geometry import Frame
from compas.geometry import Plane
from compas.geometry import Translation
from compas.robots import Joint
from compas.robots import RobotModel


# Fractal Tree Robot parameters:
initial_length = 24
n = 6
branch_angle = 0.8 #radians

# create cylinder of variable length in yz plane

def my_cylinder(length):
    radius = 1
    cylinder = Cylinder(Circle(Plane([0, 0, 0], [0, 1, 0]), radius), length)
    cylinder.transform(Translation.from_vector([0, length / 2., 0]))
    return cylinder

# create robot
model = RobotModel("robot", links=[], joints=[])

# add first link to robot and instantiate links and joints list
link0 = model.add_link("world")
links={}
joint_number = 1

# add all other links to robot
for level in range(n):
    for branch in range(2**level):
        l, b = level+1, branch+1
        print l,b
        #add link
        length = initial_length/l
        mesh = Mesh.from_shape(my_cylinder(length))
        new_link = model.add_link("link"+str(l)+str(b), visual_mesh=mesh, visual_color=(0.5-(l/(2*n)), 0.5, 0.5-(b/(2**n))))
        links.update({"link"+str(l)+str(b): new_link})
        #add first joint
        if l == 1:
            axis = (0, 0, 1)
            origin = Frame.worldXY()
            model.add_joint("joint1", Joint.CONTINUOUS, link0, new_link, origin, axis)
        #add other joints
        else:
            joint_number += 1
            origin = Frame((0, initial_length/(l-1), 0), (1, 0, 0), (0, 1, 0))
            parent_level = l-1
            parent_branch = int((((b+1)-(b+1)%2)/2))
            parent_link = model.get_link_by_name("link"+str(parent_level)+str(parent_branch))
            model.add_joint("joint"+str(joint_number), Joint.CONTINUOUS, parent_link, new_link, origin, axis)

artist = RobotModelArtist(model)

# Create a configuration object matching the number of joints in your model
names = ['joint'+str(num+1) for num in range(joint_number)]
values = [0]
for num in range(int((joint_number-1)/2)):
    values.append(branch_angle-num/17)
    values.append(-branch_angle-num/30)
configuration = Configuration.from_revolute_values(values, joint_names=names)

# Update the model using the artist
artist = RobotModelArtist(model, layer='COMPAS:assignment2')
artist.update(configuration.joint_dict)

# Render everything
artist.clear_layer()
artist.draw_visual()
artist.redraw()
