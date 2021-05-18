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
    ...
    # --- Load targets (boundaries)
    ...
    # --- Create pre-processor
    ...
    # --- slicing
    ...
    # --- Print organizer
    ...
    # --- Add attributes to mesh
    ...
    # --- Transfer mesh attributes to printpoints
    ...
    # --- Save printpoints attributes for visualization
    ...
    # --- Save printpoints dictionary to json file
    ...

    
if __name__ == "__main__":
    main()
