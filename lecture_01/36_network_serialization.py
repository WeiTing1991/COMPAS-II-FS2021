import random
from compas.datastructures import Network

network = Network()

last_node = None
for i in range(12):
    node = network.add_node(x=i // 3, y=i % 3, z=0)
    network.node_attribute(node, 'weight', random.choice(range(20)))

    if last_node:
        network.add_edge(node, i-1)
    last_node = node

print(network.summary())
print(network.to_data())
