from compas.datastructures import Network

network = Network()

network.add_edge(1, 2)
network.add_edge(2, 3)
network.add_edge(1, 4)
network.add_edge(4, 5)
network.add_edge(4, 6)

print(network.summary())
