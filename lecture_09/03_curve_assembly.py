import os
import sys
HERE = os.path.dirname(__file__)
if HERE not in sys.path:
    sys.path.append(HERE)

from compas.geometry import Bezier
from compas.geometry import Translation
from compas.geometry import Frame
from compas.geometry import Vector
from compas.geometry import Box
from compas.datastructures import Mesh
from assembly import Element
from assembly import Assembly


# Start assembly definition
assembly = Assembly()
# assembly.attributes['home_config'] = home_config
assembly.attributes['element'] = Box(Frame.worldXY(), 0.031, 0.016, 0.012)
assembly.attributes['place_tolerance'] = 0.008
assembly.approach_offset = 0.05
assembly.pick_t0cf_frame = Frame((-0.064, 0.669, 0.152), (0.001, 0.000, -1.000), (1.000, 0.000, 0.001))

source_element = assembly.attributes['element']


bezier_points = [[0.36 - 0.26, 0.0], [0.30, -0.016, 0.0], [0.67, 0.15, 0.0], [0.32, 0.29, 0.0]]
curve = Bezier(bezier_points)

N = 10
params = [i/float(N) for i in range(N + 1)]

for key, t in enumerate(params):
    point = curve.point(t)
    tangent = curve.tangent(t)
    yaxis = Vector(0, 0, 1).cross(tangent)
    frame = Frame(point, tangent, yaxis)

    x, y, z = 0, 0, (source_element.height / 2)

    frame = frame.transformed(Translation.from_vector([x, y, z]))
    approach_t0cf_frame = frame.transformed(Translation.from_vector([0, 0, assembly.approach_offset]))
    element = Element(frame=frame, approach_frame=approach_t0cf_frame, geometry_at_origin=Mesh.from_shape(source_element))
    assembly.add_element(element, key)

assembly.to_json(os.path.join(HERE, "assembly.json"))
