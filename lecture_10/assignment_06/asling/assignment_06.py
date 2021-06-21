import logging
from compas.geometry import Plane, Point, Vector, distance_point_point
from compas.datastructures import Mesh
# import compas_rhino
# from compas_rhino.geometry import RhinoLine 
# how to use compas_rhino.RhinoLine()
import os
import compas_slicer.utilities as slicer_utils
from compas_slicer.post_processing import simplify_paths_rdp, seams_smooth
from compas_slicer.slicers import ScalarFieldSlicer
import compas_slicer.utilities as utils
from compas_slicer.print_organization import ScalarFieldPrintOrganizer
from compas_slicer.print_organization import set_extruder_toggle, add_safety_printpoints
from compas_slicer.print_organization import set_linear_velocity_constant, set_blend_radius

logger = logging.getLogger('logger')
logging.basicConfig(format='%(levelname)s-%(message)s', level=logging.INFO)

DATA_PATH = os.path.join(os.path.dirname(__file__), 'data')
OUTPUT_PATH = slicer_utils.get_output_directory(DATA_PATH)
MODEL = 'tube_mesh.obj'
MODEL2 = 'sun_path.obj'

if __name__ == '__main__':
    # load mesh
    tube_mesh = Mesh.from_obj(os.path.join(DATA_PATH, MODEL))

    # Create scalar field
    sunpath_mesh = Mesh.from_obj(os.path.join(DATA_PATH, MODEL2))
    sunpath_vertices = []
    for skey in sunpath_mesh.vertices():
        sp_v = sunpath_mesh.vertex_coordinates(skey, axes='xyz')
        sunpath_vertices.append(sp_v)

    u = []
    v_coords = []
    scalar_pts = []
    for vkey in tube_mesh.vertices():
        v_coord = tube_mesh.vertex_coordinates(vkey, axes='xyz')
        v_coords.append(v_coord)
        closest = slicer_utils.get_closest_pt(v_coord, sunpath_vertices)
        scalar_pts.append(closest)
        d = distance_point_point(v_coord, closest)
        u.append(d)
    print(len(v_coords))
    print(len(scalar_pts))
    print(len(u))
    
    # want to use normals - how to get origin point of closest normal?
    # get_closest_mesh_normal_to_pt(sunpath_mesh, vkey)

    # generate contours of scalar field
    slicer = ScalarFieldSlicer(tube_mesh, u, no_of_isocurves=30)
    slicer.slice_model()
    simplify_paths_rdp(slicer, threshold=0.8)
    seams_smooth(slicer, smooth_distance=10)
    slicer_utils.save_to_json(slicer.to_data(), OUTPUT_PATH, 'isocontours.json')

    # create printpoints
    print_organizer = ScalarFieldPrintOrganizer(slicer, parameters={}, DATA_PATH=DATA_PATH)
    print_organizer.create_printpoints()

    set_extruder_toggle(print_organizer, slicer)
    add_safety_printpoints(print_organizer, z_hop=10.0)
    set_linear_velocity_constant(print_organizer, v=50.0)
    set_blend_radius(print_organizer, d_fillet=10.0)

    print_organizer.printout_info()
    printpoints_data = print_organizer.output_printpoints_dict()
    utils.save_to_json(printpoints_data, OUTPUT_PATH, 'out_printpoints.json')