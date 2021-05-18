import os
import numpy as np
from compas.datastructures import Mesh
import logging
import compas_slicer.utilities as utils
from compas_slicer.slicers import InterpolationSlicer
from compas_slicer.post_processing import simplify_paths_rdp
from compas_slicer.pre_processing import InterpolationSlicingPreprocessor
from compas_slicer.print_organization import set_extruder_toggle, set_linear_velocity_by_range
from compas_slicer.print_organization import add_safety_printpoints
from compas_slicer.pre_processing import create_mesh_boundary_attributes
from compas_slicer.print_organization import InterpolationPrintOrganizer
from compas_slicer.post_processing import seams_smooth
from compas_slicer.print_organization import smooth_printpoints_up_vectors, smooth_printpoints_layer_heights
from compas_slicer.post_processing import generate_brim
from compas.geometry import Vector, Point, normalize_vector
from compas_slicer.utilities.attributes_transfer import transfer_mesh_attributes_to_printpoints


logger = logging.getLogger('logger')
logging.basicConfig(format='%(levelname)s - %(message)s', level=logging.INFO)

DATA_PATH = os.path.join(os.path.dirname(__file__), 'data')
OUTPUT_PATH = utils.get_output_directory(DATA_PATH)
OBJ_INPUT_NAME = os.path.join(DATA_PATH, '_mesh.obj')


def main():
    # --- Load initial_mesh
    mesh = Mesh.from_obj(os.path.join(DATA_PATH, OBJ_INPUT_NAME))

    # --- Load targets (boundaries)
    low_boundary_vs = utils.load_from_json(DATA_PATH, 'boundaryLOW.json')
    high_boundary_vs = utils.load_from_json(DATA_PATH, 'boundaryHIGH.json')
    create_mesh_boundary_attributes(mesh, low_boundary_vs, high_boundary_vs)

    avg_layer_height = 10.0

    parameters = {
        'avg_layer_height': avg_layer_height,  # controls number of curves that will be generated
        'min_layer_height': 0.3,
        'max_layer_height': 5.0  # 2.0,
    }

    # --- Create pre-processor
    preprocessor = InterpolationSlicingPreprocessor(mesh, parameters, DATA_PATH)
    preprocessor.create_compound_targets()

    # --- slicing
    slicer = InterpolationSlicer(mesh, preprocessor, parameters)
    slicer.slice_model()  # compute_norm_of_gradient contours
    seams_smooth(slicer, smooth_distance=10)

    simplify_paths_rdp(slicer, threshold=0.4)
    slicer.printout_info()
    utils.save_to_json(slicer.to_data(), OUTPUT_PATH, 'curved_slicer.json')

    # --- Print organizer
    print_organizer = InterpolationPrintOrganizer(slicer, parameters, DATA_PATH)
    print_organizer.create_printpoints()

    set_linear_velocity_by_range(print_organizer, param_func=lambda ppt: ppt.layer_height,
                                 parameter_range=[avg_layer_height*0.5, avg_layer_height*2.0],
                                 velocity_range=[150, 70], bound_remapping=False)
    set_extruder_toggle(print_organizer, slicer)
    add_safety_printpoints(print_organizer, z_hop=10.0)
    smooth_printpoints_up_vectors(print_organizer, strength=0.5, iterations=10)
    smooth_printpoints_layer_heights(print_organizer, strength=0.5, iterations=5)


    # --- Add attributes to mesh
    # overhand attribute - Scalar value (per face)
    mesh.update_default_face_attributes({'overhang': 0.0})
    for f_key, data in mesh.faces(data=True):
        face_normal = mesh.face_normal(f_key, unitized=True)
        data['overhang'] = Vector(0.0, 0.0, 1.0).dot(face_normal)

    # vertex laplacian - Vector value (per vertex)
    mesh.update_default_vertex_attributes({'v_normal': 0.0})
    for v_key, data in mesh.vertices(data=True):
        n = mesh.vertex_normal(v_key)
        data['v_normal'] = Vector(*n)

    # --- Transfer mesh attributes to printpoints
    transfer_mesh_attributes_to_printpoints(mesh, print_organizer.printpoints_dict)

    # --- Save printpoints attributes for visualization
    overhangs_list = print_organizer.get_printpoints_attribute(attr_name='overhang')
    v_normal_list = print_organizer.get_printpoints_attribute(attr_name='v_normal')
    utils.save_to_json(overhangs_list, OUTPUT_PATH, 'overhangs_list.json')
    utils.save_to_json(utils.point_list_to_dict(v_normal_list), OUTPUT_PATH, 'v_normal_list.json')

    
    # --- Save printpoints dictionary to json file
    printpoints_data = print_organizer.output_printpoints_dict()
    utils.save_to_json(printpoints_data, OUTPUT_PATH, 'out_printpoints.json')

if __name__ == "__main__":
    main()
