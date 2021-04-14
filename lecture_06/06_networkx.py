import networkx as nx
from compas_plotters import NetworkPlotter
from compas.datastructures import Network

network = Network()

s = network.add_node(x=11, y=30, z=0, color=(000, 000, 000), text='black')

o = network.add_node(x=1., y=20, z=0, color=(255, 128, 000), text='orange')
g = network.add_node(x=11, y=20, z=0, color=(000, 255, 000), text='green')
p = network.add_node(x=21, y=20, z=0, color=(128, 000, 128), text='purple')

r = network.add_node(x=1., y=10, z=0, color=(255, 000, 000), text='red')
y = network.add_node(x=11, y=10, z=0, color=(255, 255, 000), text='yellow')
b = network.add_node(x=21, y=10, z=0, color=(000, 000, 255), text='blue')

w = network.add_node(x=11, y=00, z=0, color=(255, 255, 255), text='white')

network.add_edge(w, r)
network.add_edge(w, y)
network.add_edge(w, b)

network.add_edge(r, o)
network.add_edge(r, p)

network.add_edge(y, o)
network.add_edge(y, g)

network.add_edge(b, g)
network.add_edge(b, p)

network.add_edge(o, s)
network.add_edge(g, s)
network.add_edge(p, s)

print(network.summary())

# Convert back and forth
dg = network.to_networkx()
print(type(dg))
print('Closeness centrality:')
print(nx.closeness_centrality(dg))

network = Network.from_networkx(dg)

node_color = network.nodes_attribute('color')
labels = network.nodes_attribute('text')

plotter = NetworkPlotter(network, figsize=(12, 7.5))
plotter.defaults['node.radius'] = 1.5
plotter.draw_nodes(
    text=dict(zip(network.nodes(), labels)),
    textcolor={s: (1, 1, 1), b: (1, 1, 1), p: (1, 1, 1)},
    facecolor=dict(zip(network.nodes(), node_color)))
plotter.draw_edges()
plotter.show()
