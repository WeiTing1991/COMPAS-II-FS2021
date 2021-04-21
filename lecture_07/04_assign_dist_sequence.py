import math
import os
from itertools import combinations

import compas

HERE = os.path.dirname(__file__)

# Load assembly
filename = os.path.join(HERE, 'assembly.json')
assembly = compas.json_load(filename)

# Reset assembly connectivity
assembly.edge = {i: {} for i in assembly.nodes()}
assembly.adjacency = {i: {} for i in assembly.nodes()}

edges = list(assembly.edges())
for u, v in edges:
    assembly.delete_edge(u, v)

z_delta = .013
y_delta = .0175
epsilon = .0001

threshold = math.sqrt(z_delta**2 + y_delta**2) + epsilon

for key1, key2 in combinations(assembly.node, 2):
    frame1 = assembly.node_attribute(key1, 'element').frame
    frame2 = assembly.node_attribute(key2, 'element').frame

    if frame1.point.distance_to_point(frame2.point) < threshold:
        if frame2.point.z == frame1.point.z:
            continue
        if frame1.point.z < frame2.point.z:
            assembly.add_edge(key2, key1)
        if frame2.point.z < frame1.point.z:
            assembly.add_edge(key1, key2)

# Save assembly
compas.json_dump(assembly, filename)
