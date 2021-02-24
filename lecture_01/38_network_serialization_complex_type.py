import random

from compas.datastructures import Datastructure
from compas.datastructures import Network


class Weight(Datastructure):
    def __init__(self, value=None):
        self.value = value or random.choice(range(20))

    @property
    def data(self):
        return {'value': self.value}

    @data.setter
    def data(self, data):
        self.value = data['value']


network = Network()

last_node = None
for i in range(12):
    node = network.add_node(x=i // 3, y=i % 3, z=0)
    network.node_attribute(node, 'weight', Weight())

    if last_node:
        network.add_edge(node, i-1)
    last_node = node

print(network.summary())
# print(network.to_data())

network.to_json(__file__ + '.json')

network2 = Network.from_json(__file__ + '.json')
print(network2.summary())
# print(network2.to_data())
