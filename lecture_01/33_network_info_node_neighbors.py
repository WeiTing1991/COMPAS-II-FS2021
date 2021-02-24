import compas
from compas.datastructures import Network
from compas_plotters import NetworkPlotter

network = Network.from_obj(compas.get('grid_irregular.obj'))

node = next(network.nodes())
nbrs = network.neighbors(node)

facecolor = {node: (255, 0, 0)}
for nbr in nbrs:
    facecolor[nbr] = (0, 0, 255)

edgecolor = {}
for nbr in nbrs:
    edgecolor[node, nbr] = (0, 255, 0)
    edgecolor[nbr, node] = (0, 255, 0)

plotter = NetworkPlotter(network, figsize=(12, 7.5))
plotter.draw_nodes(facecolor=facecolor)
plotter.draw_edges(color=edgecolor, width={edge: 2.0 for edge in edgecolor})
plotter.show()
