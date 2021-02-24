import math
from compas.geometry import Point
from compas.geometry import Vector
from compas.geometry import Rotation
from compas.datastructures import Network
from compas_plotters import NetworkPlotter

lsys = "A-A++A-A-A-A++A-A++A-A++A-A-A-A++A-A-A-A++A-A-A-A++A-A++A-A++A-A-A-A++A-A++A-A++A-A-A-A++A-A++A-A++A-A-A-A++A-A-A-A++A-A-A-A++A-A++A-A++A-A-A-A++A"

network = Network()
step = 1.
pt = Point(0, 0, 0)
v = Vector(1, 0, 0)


def draw(network, point, vector, s, step, last_node=None):
    for i, c in enumerate(s):
        if c == 'A':
            point = point + vector * step
            a = network.add_node(x=point.x, y=point.y, z=point.z)
            if last_node:
                network.add_edge(last_node, a)
            last_node = a
        elif c == '-':
            R = Rotation.from_axis_and_angle((0, 0, 1), math.radians(60))
            vector.transform(R)
        elif c == '+':
            R = Rotation.from_axis_and_angle((0, 0, 1), math.radians(-60))
            vector.transform(R)


draw(network, pt, v, lsys, step)

plotter = NetworkPlotter(network, figsize=(12, 7.5))
plotter.draw_nodes(radius=0.1)
plotter.draw_edges()
plotter.show()
