import os

from compas_fab.robots import AttachedCollisionMesh
from compas_fab.robots import CollisionMesh
from compas_fab.robots import Tool

import compas
from compas.datastructures import Mesh
from compas.geometry import Frame

HERE = os.path.dirname(__file__)
Z_OFFSET = 0.070


def get_last_config(trajectory, robot):
    start_configuration = robot.zero_configuration()

    if trajectory and trajectory.points:
        start_configuration.values = trajectory.points[-1].values

    return start_configuration


def attach_vacuum_gripper(scene):
    # create tool from mesh and frame
    mesh = Mesh.from_stl(os.path.join(HERE, 'vacuum_gripper.stl'))
    frame = Frame([Z_OFFSET, 0, 0], [0, 0, 1], [0, 1, 0])
    tool = Tool(mesh, frame, name='vacuum_gripper')

    scene.robot.attach_tool(tool)
    scene.add_attached_tool()


def add_static_objects(scene):
    meshes = compas.json_load(os.path.join(HERE, 'static-objects.json'))
    scene.remove_collision_mesh('static_objects')

    for mesh in meshes:
        cm = CollisionMesh(mesh, 'static_objects')
        scene.append_collision_mesh(cm)

def add_built_elements(scene, assembly, built_elements):
    scene.remove_collision_mesh('built_elements')

    for key in built_elements:
        element = assembly.element(key)
        cm = CollisionMesh(element.geometry_at_placement, 'built_elements')
        scene.append_collision_mesh(cm)
        print('.', end='', flush=True)

    # Setup attached element
    scene.remove_attached_collision_mesh('brick')
    scene.remove_collision_mesh('brick')

    ee_link_name = scene.robot.get_end_effector_link_name()
    if scene.robot.attached_tool:
        brick_frame = scene.robot.attached_tool.frame.copy()
    else:
        brick_frame = Frame.worldXY()

    # Centered origin, get half
    element = assembly.attributes['element']
    brick_frame.point.x += element.height / 2
    element_mesh = Mesh.from_shape(element)
    brick_acm = AttachedCollisionMesh(CollisionMesh(element_mesh, 'brick', brick_frame), ee_link_name)
    scene.add_attached_collision_mesh(brick_acm)
