import compas
from compas.datastructures import Network
from compas_plotters import NetworkPlotter

network = Network.from_obj(compas.get('grid_irregular.obj'))
text = {node: str(node) for node in network.nodes()}

plotter = NetworkPlotter(network, figsize=(12, 7.5))

plotter.draw_nodes(text=text, radius=0.2)
plotter.draw_edges()
plotter.show()
