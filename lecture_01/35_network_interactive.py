import random

from compas_plotters import NetworkPlotter

import compas
from compas.datastructures import Network
from compas.utilities import pairwise

network = Network.from_obj(compas.get('grid_irregular.obj'))
goal = random.choice(list(network.leaves()))

plotter = NetworkPlotter(network, figsize=(10, 8))
plotter.draw_nodes(radius=0.1, picker=10)
plotter.draw_edges()

default_colors = [plotter.defaults['node.facecolor'] for key in network.nodes()]
highlight_color = '#ff0000'
default_colors[goal] = highlight_color

default_linewidths = [plotter.defaults['edge.width'] for key in network.edges()]
highlight_width = 3 * plotter.defaults['edge.width']

index_node = network.index_key()
edge_index = network.uv_index()
edge_index.update({(v, u): index for (u, v), index in edge_index.items()})

plotter.nodecollection.set_facecolor(default_colors)


def on_pick(event):
    index = event.ind[0]
    start = index_node[index]

    nodes = network.shortest_path(start, goal)

    colors = default_colors[:]
    widths = default_linewidths[:]

    colors[start] = highlight_color
    for u, v in pairwise(nodes):
        colors[v] = highlight_color
        widths[edge_index[u, v]] = highlight_width

    plotter.nodecollection.set_facecolor(colors)
    plotter.edgecollection.set_linewidths(widths)
    plotter.update()


plotter.register_listener(on_pick)
plotter.show()
