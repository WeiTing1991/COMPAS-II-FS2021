import os

import compas

HERE = os.path.dirname(__file__)

# Load assembly
filename = os.path.join(HERE, 'assembly.json')
assembly = compas.json_load(filename)

for key in assembly.nodes():
    e = assembly.element(key)
    e.trajectory = None

# Save assembly
compas.json_dump(assembly, filename)
