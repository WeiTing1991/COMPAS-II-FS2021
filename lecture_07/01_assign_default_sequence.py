import os

import compas

HERE = os.path.dirname(__file__)

# Load assembly
filename = os.path.join(HERE, 'assembly.json')
assembly = compas.json_load(filename)

# Reset assembly connectivity
assembly.edge = {i: {} for i in assembly.nodes()}
assembly.adjacency = {i: {} for i in assembly.nodes()}

# Define connectivity as a linear sequence dependant on implementation details (never a good idea!)
linear_sequence = list(assembly.nodes())
for i, key in enumerate(linear_sequence):
    if i < len(linear_sequence) - 1:
        assembly.add_edge(key, linear_sequence[i + 1])

# Save assembly
compas.json_dump(assembly, filename)
