import os

from compas_rhino.artists import NetworkArtist

import compas

HERE = os.path.dirname(__file__)

# Load assembly
filename = os.path.join(HERE, 'assembly.json')
assembly = compas.json_load(filename)

print(assembly.summary())

labels = list(assembly.nodes())

artist = NetworkArtist(assembly, layer='assembly')
artist.clear_layer()
artist.draw_nodelabels(
    text=dict(zip(assembly.nodes(), labels)))
artist.draw_edges()
artist.draw()
artist.redraw()

