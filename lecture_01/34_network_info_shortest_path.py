import random
import compas
from compas.datastructures import Network
from compas.utilities import pairwise
from compas_plotters import NetworkPlotter

network = Network.from_obj(compas.get('grid_irregular.obj'))
plotter = NetworkPlotter(network, figsize=(12, 7.5))

nodecolor = (0, 255, 0)
edgecolor = (0, 255, 0)
edgewidth = 3 * plotter.defaults['edge.width']

node_color = {}
edge_color = {}
edge_width = {}

start = random.choice(list(network.leaves()))
goal = random.choice(list(network.leaves()))
nodes = network.shortest_path(start, goal)

for u, v in pairwise(nodes):
    node_color[v] = nodecolor
    edge_color[u, v] = edge_color[v, u] = edgecolor
    edge_width[u, v] = edge_width[v, u] = edgewidth

node_color[start] = (255, 0, 0)
node_color[goal] = (0, 0, 255)

plotter.draw_nodes(facecolor=node_color)
plotter.draw_edges(color=edge_color, width=edge_width)
plotter.show()
