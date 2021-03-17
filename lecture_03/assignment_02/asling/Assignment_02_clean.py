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
wheel.transform(Translation.from_vector([width/2, 0, 0]))
wheel2 = wheel

# create capsule in yz plane = body
radius, line = 500, Line((0,0,0), (0,0,1000))
body = Capsule(line, radius)
body.transform(Translation.from_vector([body.radius, 0, 0]))

# create sphere in yz plane = head
point, radius = (0,0,0), 540
head = Sphere(point, radius)
head.transform(Translation.from_vector([0, 0, 0]))

# create sphere in yz plane = shoulders 
point, radius = (0,0,0), 160
shoulder = Sphere(point, radius)
shoulder.transform(Translation.from_vector([shoulder.radius,0,0]))
shoulder2 = shoulder.transformed(Translation.from_vector([-2*shoulder.radius,0,0]))

# create cylinders in yz plane = arms
radius, length = 125, 1000
arm = Cylinder(Circle(Plane([0, 0, 0], [1, 0, 0]), radius), length)
arm.transform(Translation.from_vector([arm.height/2, 0, 0]))
arm2 = arm.transformed(Translation.from_vector([-arm.height, 0, 0]))

# create robot
model = RobotModel("Otto", links=[], joints=[])

# add first link to Otto, reference to world 
link0 = model.add_link("world")  
# axis 
axisZ = (0, 0, 1)
axisX = (1, 0, 0)
axisY = (0, 1, 0)

# add second link to Otto - wheel
mesh = Mesh.from_shape(wheel)
link1 = model.add_link("link1", visual_mesh=mesh, visual_color=(0.2, 0.5, 0.6))
origin = Frame.worldXY()  # origin of XY plane
model.add_joint("joint1", Joint.CONTINUOUS, link0, link1, origin, axisZ)

# add body & joint
mesh = Mesh.from_shape(body)
link2 = model.add_link("link2", visual_mesh=mesh, visual_color=(0.5, 0.6, 0.2))
origin = Frame((wheel.height, 0, 0), (1, 0, 0), (0, 1, 0))
model.add_joint("joint2", Joint.CONTINUOUS, link1, link2, origin, axisZ)

# add wheel2 & joint
mesh = Mesh.from_shape(wheel2)
link3 = model.add_link("link3", visual_mesh=mesh, visual_color=(0.2, 0.5, 0.6))
origin = Frame((2*body.radius, 0, 0), (1, 0, 0), (0, 1, 0))
model.add_joint("joint3", Joint.CONTINUOUS, link2, link3, origin, axisZ)

# add shoulder & joint
mesh = Mesh.from_shape(shoulder)
link4 = model.add_link("link4", visual_mesh=mesh, visual_color=(0.5, 0.7, 0.9))
origin = Frame((0, 0, line.length), (1, 0, 0), (0, 1, 0))
model.add_joint("joint4", Joint.CONTINUOUS, link3, link4, origin, axisZ)

# add arm & joint
mesh = Mesh.from_shape(arm)
link5 = model.add_link("link5", visual_mesh=mesh, visual_color=(0.5, 0.6, 0.2))
origin = Frame((shoulder.radius*2, 0, 0), (1, 0, 0), (0, 1, 0))
model.add_joint("joint5", Joint.CONTINUOUS, link4, link5, origin, axisZ)

# add head & joint
mesh = Mesh.from_shape(head)
link6 = model.add_link("link6", visual_mesh=mesh, visual_color=(0.5, 0.6, 0.2))
origin = Frame((-(body.radius+shoulder.radius*2), 0, body.radius+head.radius), (1, 0, 0), (0, 1, 0))
model.add_joint("joint6", Joint.CONTINUOUS, link5, link6, origin, axisZ)

# add shoulder2 & joint
mesh = Mesh.from_shape(shoulder2)
link7 = model.add_link("link7", visual_mesh=mesh, visual_color=(0.5, 0.7, 0.9))
origin = Frame((-body.radius, 0, -(body.radius+head.radius)), (1, 0, 0), (0, 1, 0))
model.add_joint("joint7", Joint.CONTINUOUS, link6, link7, origin, axisZ)

# add arm2 & joint
mesh = Mesh.from_shape(arm2)
link8 = model.add_link("link8", visual_mesh=mesh, visual_color=(0.5, 0.6, 0.2))
origin = Frame((-shoulder.radius*2, 0, 0), (1, 0, 0), (0, 1, 0))
model.add_joint("joint8", Joint.CONTINUOUS, link7, link8, origin, axisZ)

# Create a configuration object matching the number of joints in your model
configuration = Configuration.from_revolute_values([0.3, -0.3, 0.3, 0.2, -0.9, 0.5, 0.2, 0.9], joint_names=['joint1', 'joint2', 'joint3', 'joint4', 'joint5', 'joint6', 'joint7', 'joint8'])

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