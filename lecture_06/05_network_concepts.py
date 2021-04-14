from compas.datastructures import Network

network = Network()

# Nodes
s = network.add_node(x=11, y=30, z=0, color=(000, 000, 000), text='black')

o = network.add_node(x=1., y=20, z=0, color=(255, 128, 000), text='orange')
g = network.add_node(x=11, y=20, z=0, color=(000, 255, 000), text='green')
p = network.add_node(x=21, y=20, z=0, color=(128, 000, 128), text='purple')

r = network.add_node(x=1., y=10, z=0, color=(255, 000, 000), text='red')
y = network.add_node(x=11, y=10, z=0, color=(255, 255, 000), text='yellow')
b = network.add_node(x=21, y=10, z=0, color=(000, 000, 255), text='blue')

w = network.add_node(x=11, y=00, z=0, color=(255, 255, 255), text='white')

# Edges
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

# Degree
print('Orange, in-degree', network.degree_in(o))
print('Orange, out-degree', network.degree_out(o))
print('Orange, degree', network.degree(o))

# Neighbors
print('Red, neighbors', network.neighbors(r))
print('Red, out-neighbors', network.neighbors_out(r))

# Attributes
print('Yellow, xyz attributes', network.node_attributes(y, ['x', 'y', 'z']))
print('Yellow, xyz attributes', network.node_coordinates(y))

# Queries
print(list(network.nodes_where({'y': 10})))
print(list(network.edges_where_predicate(lambda uv, d: uv[1] == r)))
