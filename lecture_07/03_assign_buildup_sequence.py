import os

import compas
from compas.topology.traversal import breadth_first_ordering, breadth_first_tree

HERE = os.path.dirname(__file__)

# Load assembly
filename = os.path.join(HERE, 'assembly.json')
assembly = compas.json_load(filename)

# Reset assembly connectivity
assembly.edge = {i: {} for i in assembly.nodes()}
assembly.adjacency = {i: {} for i in assembly.nodes()}

# Define connectivity as a linear sequence
linear_sequence = sorted(assembly.nodes())
COURSES = 12
BRICKS_PER_COURSE = 21
for course in range(COURSES):
    for i in range(BRICKS_PER_COURSE):
        key = i + (course * BRICKS_PER_COURSE)
        assembly.node_attribute(key, 'course', course)

for key in assembly.nodes():
    course = assembly.node_attribute(key, 'course')
    next_course = set(assembly.nodes_where({'course': course + 1}))
    if course % 2 == 0:
        offsets = (BRICKS_PER_COURSE - 1, BRICKS_PER_COURSE)
    else:
        offsets = (BRICKS_PER_COURSE, BRICKS_PER_COURSE + 1)
    nbrs_up = set([key + offsets[0], key + offsets[1]]).intersection(next_course)
    for nbr in nbrs_up:
        assembly.add_edge(key, nbr)

# Save assembly
compas.json_dump(assembly, filename)
