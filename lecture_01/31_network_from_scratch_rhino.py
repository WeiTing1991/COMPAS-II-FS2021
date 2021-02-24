import random

from compas_rhino.artists import NetworkArtist
from compas.datastructures import Network

network = Network()

network.add_edge(1, 2)
network.add_edge(2, 3)
network.add_edge(1, 4)
network.add_edge(4, 5)
network.add_edge(4, 6)

for node in network.nodes():
    x = random.choice(range(5))
    y = random.choice(range(5))
    z = random.choice(range(5))
    network.node_attributes(node, 'xyz', [x, y, z])

print(network.summary())

text = {node: str(node) for node in network.nodes()}

artist = NetworkArtist(network, layer='network')
artist.clear_layer()
artist.draw_nodelabels(text)
artist.draw()
artist.redraw()
