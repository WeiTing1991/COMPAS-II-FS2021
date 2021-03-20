# Rhino
from compas_fab.robots import Configuration
from compas_rhino.artists import RobotModelArtist, CapsuleArtist, SphereArtist, CylinderArtist, FrameArtist

from compas.datastructures import Mesh
from compas.geometry import Circle, Line
from compas.geometry import Cylinder, Capsule, Sphere
from compas.geometry import Frame
from compas.geometry import Plane, Point, Vector
from compas.geometry import Translation, Reflection
from compas.robots import Joint
from compas.robots import RobotModel

# units in mm
# create cylinder in yz plane = wheel
radius, width = 600, 100
wheel = Cylinder(Circle(Plane([0, 0, 0], [1, 0, 0]), radius), width)

# create capsule in yz plane = body
radius, line = 500, Line((0,0,0), (0,0,1000))
body = Capsule(line, radius)

# create sphere in yz plane = head
point, radius = (0,0,0), 540
head = Sphere(point, radius)

# create sphere in yz plane = shoulders 
point, radius = (0,0,0), 160
shoulder = Sphere(point, radius)

# create cylinders in yz plane = arms
radius, length = 125, 1000
arm = Cylinder(Circle(Plane([0, 0, 0], [1, 0, 0]), radius), length)
arm.transform(Translation.from_vector([-arm.height/2, 0, 0]))
arm2 = arm.transformed(Translation.from_vector([arm.height, 0, 0]))

# # test draw shapes
# artist1 = CylinderArtist(wheel)
# artist2 = CylinderArtist(wheel2)
# artist3 = CapsuleArtist(body)
# artist4 = SphereArtist(head)
# artist5 = SphereArtist(shoulder)
# artist6 = SphereArtist(shoulder2)
# artist7 = CylinderArtist(arm)
# artist8 = CylinderArtist(arm2)

# # Render everything
# artist1.draw()
# artist2.draw()
# artist3.draw()
# artist4.draw()
# artist5.draw()
# artist6.draw()
# artist7.draw()
# artist8.draw()

# create robot
model = RobotModel("Otto", links=[], joints=[])

# add first link to Otto, reference to world 
link0 = model.add_link("world")  
# axis 
axisZ = (0, 0, 1)
axisX = (1, 0, 0)
axisY = (0, 1, 0)

# add second link to Otto - body
mesh = Mesh.from_shape(body)
link1 = model.add_link("link1", visual_mesh=mesh, visual_color=(0.5, 0.6, 0.2))
origin = Frame.worldXY()  # origin of XY plane
model.add_joint("joint1", Joint.FIXED, link0, link1, origin, axisZ)

# add wheel & joint
mesh = Mesh.from_shape(wheel)
link2 = model.add_link("link2", visual_mesh=mesh, visual_color=(0.2, 0.5, 0.6))
origin = Frame((-body.radius-wheel.height/2, 0, 0), (1, 0, 0), (0, 1, 0))
model.add_joint("joint2", Joint.CONTINUOUS, link1, link2, origin, axisZ) # should be revolute
model.add_joint("joint9", Joint.CONTINUOUS, link1, link2, origin, axisX)

# add shoulder & joint
mesh = Mesh.from_shape(shoulder)
link3 = model.add_link("link3", visual_mesh=mesh, visual_color=(0.5, 0.7, 0.9))
origin = Frame((-body.radius-shoulder.radius, 0, line.length), (1, 0, 0), (0, 1, 0))
model.add_joint("joint3", Joint.CONTINUOUS, link1, link3, origin, axisZ)
model.add_joint("joint11", Joint.CONTINUOUS, link1, link3, origin, axisX)
model.add_joint("joint12", Joint.CONTINUOUS, link1, link3, origin, axisY)

# add arm & joint
mesh = Mesh.from_shape(arm)
link4 = model.add_link("link4", visual_mesh=mesh, visual_color=(0.5, 0.6, 0.9))
origin = Frame((-shoulder.radius, 0, 0), (1, 0, 0), (0, 1, 0))
model.add_joint("joint4", Joint.CONTINUOUS, link3, link4, origin, axisY)

# add head & joint
mesh = Mesh.from_shape(head)
link5 = model.add_link("link5", visual_mesh=mesh, visual_color=(0.5, 0.6, 0.2))
origin = Frame((0, 0, body.radius+head.radius+line.length), (1, 0, 0), (0, 1, 0))
model.add_joint("joint5", Joint.CONTINUOUS, link1, link5, origin, axisZ)

# add wheel2 & joint
mesh = Mesh.from_shape(wheel)
link6 = model.add_link("link6", visual_mesh=mesh, visual_color=(0.9, 0.5, 0.6))
origin = Frame((body.radius+0.5*wheel.height, 0, 0), (1, 0, 0), (0, 1, 0))
model.add_joint("joint6", Joint.CONTINUOUS, link1, link6, origin, axisZ) # should be revolute
model.add_joint("joint10", Joint.CONTINUOUS, link1, link6, origin, axisX)

# add shoulder2 & joint
mesh = Mesh.from_shape(shoulder)
link7 = model.add_link("link7", visual_mesh=mesh, visual_color=(0.9, 0.7, 0.9))
origin = Frame((body.radius+shoulder.radius, 0, line.length), (1, 0, 0), (0, 1, 0))
model.add_joint("joint7", Joint.CONTINUOUS, link1, link7, origin, axisZ)
model.add_joint("joint13", Joint.CONTINUOUS, link1, link7, origin, axisX)
model.add_joint("joint14", Joint.CONTINUOUS, link1, link7, origin, axisY)

# add arm2 & joint
mesh = Mesh.from_shape(arm2)
link8 = model.add_link("link8", visual_mesh=mesh, visual_color=(0.9, 0.6, 0.2))
origin = Frame((shoulder.radius, 0, 0), (1, 0, 0), (0, 1, 0))
model.add_joint("joint8", Joint.CONTINUOUS, link7, link8, origin, axisY)

# Create a configuration object matching the number of joints in your model
joint_values = [0, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5]
joints = ['joint1', 'joint2', 'joint3', 'joint4', 'joint5', 'joint6', 'joint7', 'joint8', 'joint9', 'joint10', 'joint11', 'joint12', 'joint13', 'joint14']
configuration = Configuration.from_revolute_values(joint_values, joints)

# Update the model using the artist
artist = RobotModelArtist(model)
artist.update(configuration.joint_dict)

# Render everything
artist.draw_visual()
artist.redraw()

# draw frames
for frame in model.transformed_frames(dict()):
    fartist = FrameArtist(frame, layer='COMPAS::Robot Viz', scale=0.1)
    fartist.draw()