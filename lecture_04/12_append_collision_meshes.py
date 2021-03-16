import time

from compas.datastructures import Mesh
from compas.geometry import Box, Translation

from compas_fab.backends import RosClient
from compas_fab.robots import CollisionMesh
from compas_fab.robots import PlanningScene

with RosClient('localhost') as client:
    robot = client.load_robot()
    scene = PlanningScene(robot)

    brick = Box.from_width_height_depth(0.016, 0.012, 0.031)
    brick.transform(Translation.from_vector([0, 0, brick.zsize / 2.]))

    for i in range(5):
        mesh = Mesh.from_shape(brick)
        cm = CollisionMesh(mesh, 'brick_wall')
        cm.frame.point.y += 0.5
        cm.frame.point.z += brick.zsize * i

        scene.append_collision_mesh(cm)

    # sleep a bit before terminating the client
    time.sleep(1)
