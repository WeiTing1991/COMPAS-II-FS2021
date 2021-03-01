from compas.geometry import Rotation
from compas.geometry import Quaternion

q = Quaternion(0.918958, -0.020197, -0.151477, 0.363544)
print(q.is_unit)
R = Rotation.from_quaternion(q)
print(R.quaternion == q)