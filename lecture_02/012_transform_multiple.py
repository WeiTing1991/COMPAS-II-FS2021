import time
import compas
from compas.datastructures import Mesh
from compas.geometry import Rotation
from compas.geometry import transform_points
from compas.geometry import transform_points_numpy

# load mesh
mesh = Mesh.from_ply(compas.get('bunny.ply'))
v, f = mesh.to_vertices_and_faces()
print("The mesh has {} vertices.".format(len(v)))

# create Transformation
T = Rotation.from_axis_and_angle([-0.248, -0.786, -0.566], 2.78, point=[1.0, 0.0, 0.0])

# transform points with transform_points
t0 = time.time()
transform_points(v, T)
print("transfrom_points takes {:.4f} seconds.".format(time.time() - t0))

# transform points with transform_points_numpy
t0 = time.time()
transform_points_numpy(v, T)
print("transfrom_points_numpy takes {:.4f} seconds.".format(time.time() - t0))
