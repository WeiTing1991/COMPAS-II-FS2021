# Access numpy from Rhino
from compas.rpc import Proxy

np = Proxy('numpy', python='python')
an_array = np.array([[1, 2], [3, 5]])
print(np.mean(an_array))

# np.stop_server()
