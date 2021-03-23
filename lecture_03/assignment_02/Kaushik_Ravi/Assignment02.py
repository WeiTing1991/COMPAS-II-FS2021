import math

from compas.datastructures import Mesh

from compas.geometry import Point, Vector, Frame, Circle, Plane, Line
from compas.geometry import Cylinder, Box
from compas.geometry import Transformation, Translation

from compas.utilities import pairwise

from compas.robots import RobotModel
from compas.robots import Joint

from compas_rhino.artists import FrameArtist, LineArtist, CylinderArtist
from compas_rhino.artists import RobotModelArtist

# ==============================================================================
# Model
# ==============================================================================

robot = RobotModel('Robot-Hand')

# ==============================================================================
# Links
# ==============================================================================

cylinder = Cylinder(Circle(Plane(Point(0, 0, 0), Vector(0, 0, 1)), 0.5), 0.02)
mesh = Mesh.from_shape(cylinder, u=32)
base = robot.add_link(
    'base',
    visual_meshes=[mesh],
    visual_color=(0.1, 0.1, 0.1)
)

cylinder = Cylinder(Circle(Plane(Point(0, 0, 0), Vector(0, 0, 1)), 0.2), 0.5)
cylinder.transform(Translation.from_vector([0, 0, 0.25]))
mesh = Mesh.from_shape(cylinder, u=24)
shoulder = robot.add_link(
    'shoulder',
    visual_meshes=[mesh],
    visual_color=(0, 0, 1.0)
)

cylinder = Cylinder(Circle(Plane(Point(0, 0, 0), Vector(0, 0, 1)), 0.08), 1.0)
cylinder.transform(Translation.from_vector([0, 0, 0.5]))
mesh = Mesh.from_shape(cylinder)
arm = robot.add_link(
    'arm',
    visual_meshes=[mesh],
    visual_color=(0.0, 1.0, 1.0)
)

cylinder = Cylinder(Circle(Plane(Point(0, 0, 0), Vector(0, 0, 1)), 0.08), 1.0)
cylinder.transform(Translation.from_vector([0, 0, 0.5]))
mesh = Mesh.from_shape(cylinder)
forearm = robot.add_link(
    'forearm',
    visual_meshes=[mesh],
    visual_color=(0.0, 1.0, 1.0)
)

cylinder = Cylinder(Circle(Plane(Point(0, 0, 0), Vector(0, 0, 1)), 0.11), 0.01)
mesh = Mesh.from_shape(cylinder, u=32)
wrist = robot.add_link(
    'wrist',
    visual_meshes=[mesh],
    visual_color=(0.1, 0.1, 0.1)
)

box = Box.from_width_height_depth(0.04, 0.3, 0.22)
box.transform(Translation.from_vector([0, 0, 0.15]))
mesh = Mesh.from_shape(box)
hand = robot.add_link(
    'hand',
    visual_meshes=[mesh],
    visual_color=(0, 0, 1.0)
)

# ==============================================================================
# Joints
# ==============================================================================

base_joint = robot.add_joint(
    'base-shoulder',
    Joint.REVOLUTE,
    base, shoulder,
    origin=Frame(Point(0, 0, 0), Vector(1, 0, 0), Vector(0, 1, 0)),
    axis=Vector(0, 0, 1),
    limit=(-0.5 * math.pi, +0.5 * math.pi)
)

shoulder_joint = robot.add_joint(
    'shoulder-arm',
    Joint.REVOLUTE,
    shoulder, arm,
    origin=Frame(Point(0, 0, 0.5), Vector(1, 0, 0), Vector(0, 1, 0)),
    axis=Vector(0, 1, 0),
    limit=(-0.5 * math.pi, +0.5 * math.pi)
)

elbow_joint = robot.add_joint(
    'arm-forearm',
    Joint.REVOLUTE,
    arm, forearm,
    origin=Frame(Point(0, 0, 1.0), Vector(1, 0, 0), Vector(0, 1, 0)),
    axis=Vector(0, 1, 0),
    limit=(-0.5 * math.pi, +0.5 * math.pi)
)

wrist_joint = robot.add_joint(
    'forearm-wrist',
    Joint.REVOLUTE,
    forearm, wrist,
    origin=Frame(Point(0, 0, 1.0), Vector(1, 0, 0), Vector(0, 1, 0)),
    axis=Vector(0, 1, 0),
    limit=(-0.5 * math.pi, +0.5 * math.pi)
)

hand_joint = robot.add_joint(
    'wrist-hand',
    Joint.CONTINUOUS,
    wrist, hand,
    origin=Frame(Point(0, 0, 0.0), Vector(1, 0, 0), Vector(0, 1, 0)),
    axis=Vector(0, 0, 1)
)

# ==============================================================================
# State
# ==============================================================================

names = robot.get_configurable_joint_names()
values = [+0.25 * math.pi, -0.25 * math.pi, +0.5 * math.pi, 0, +0.25 * math.pi]
state = dict(zip(names, values))

transformations = robot.compute_transformations(state)

frames = []
axes = []

for joint in robot.iter_joints():
    frame = joint.origin.transformed(transformations[joint.name])
    frame.name = joint.name
    frames.append(frame)

    axis = joint.axis.transformed(transformations[joint.name])
    axis.name = joint.name
    axes.append(axis)


artist = RobotModelArtist(robot, layer="Robot")
artist.clear_layer()
artist.update(state, collision=False)
artist.draw()
