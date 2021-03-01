"""Example: Create a rotation from and axis and an angle.
"""
from compas.geometry import Vector
from compas.geometry import Rotation

aav = Vector(-0.043, -0.254, 0.617)
angle, axis = aav.unitized(), aav.length
print(angle, axis)

R = Rotation.from_axis_angle_vector(aav)
axis, angle = R.axis_and_angle
print(axis, angle)
