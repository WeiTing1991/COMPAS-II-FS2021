"""There are several ways to construct a `Frame`.
"""
from compas.geometry import Point
from compas.geometry import Vector
from compas.geometry import Frame
from compas.geometry import Plane

# Frame autocorrects axes to be orthonormal
F = Frame(Point(1, 0, 0), Vector(-0.45, 0.1, 0.3), Vector(1, 0, 0))

F = Frame([1, 0, 0], [-0.45, 0.1, 0.3], [1, 0, 0])

F = Frame.from_points([1, 1, 1], [2, 3, 6], [6, 3, 0])
F = Frame.from_plane(Plane([0, 0, 0], [0.5, 0.2, 0.1]))
F = Frame.from_euler_angles([0.5, 1., 0.2])
F = Frame.worldXY()

