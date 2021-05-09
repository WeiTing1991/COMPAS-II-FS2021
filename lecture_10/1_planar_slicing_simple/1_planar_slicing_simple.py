import time
import os
import logging

import compas_slicer.utilities as utils
from compas_slicer.pre_processing import move_mesh_to_point
from compas_slicer.slicers import PlanarSlicer
from compas_slicer.post_processing import generate_brim
from compas_slicer.post_processing import generate_raft
from compas_slicer.post_processing import simplify_paths_rdp
from compas_slicer.post_processing import seams_smooth
from compas_slicer.print_organization import PlanarPrintOrganizer
from compas_slicer.print_organization import set_extruder_toggle
from compas_slicer.print_organization import add_safety_printpoints
from compas_slicer.print_organization import set_linear_velocity_constant
from compas_slicer.print_organization import set_blend_radius
from compas_slicer.utilities import save_to_json

from compas.datastructures import Mesh
from compas.geometry import Point

# ==============================================================================
# Logging
# ==============================================================================
logger = logging.getLogger('logger')
logging.basicConfig(format='%(levelname)s-%(message)s', level=logging.INFO)

# ==============================================================================
# Select location of data folder and specify model to slice
# ==============================================================================
DATA = os.path.join(os.path.dirname(__file__), 'data')
OUTPUT_DIR = utils.get_output_directory(DATA)  # creates 'output' folder if it doesn't already exist
MODEL = 'simple_vase_open_low_res.obj'


def main():
    start_time = time.time()

    # ==========================================================================
    # Load mesh
    # ==========================================================================
    compas_mesh = ...

    # ==========================================================================
    # Move to origin
    # ==========================================================================
    ...

    # ==========================================================================
    # Slicing
    # options: 'default': Both for open and closed paths. But slow
    #          'cgal':    Very fast. Only for closed paths.
    #                     Requires additional installation (compas_cgal).
    # ==========================================================================
    slicer = ...
    ...

    # ==========================================================================
    # Generate brim / raft
    # ==========================================================================
    ...

    # ==========================================================================
    # Simplify the paths by removing points with a certain threshold
    # change the threshold value to remove more or less points
    # ==========================================================================
    ...

    # ==========================================================================
    # Smooth the seams between layers
    # change the smooth_distance value to achieve smoother, or more abrupt seams
    # ==========================================================================
    ...

    # ==========================================================================
    # Prints out the info of the slicer
    # ==========================================================================
    ...

    # ==========================================================================
    # Save slicer data to JSON
    # ==========================================================================
    ...

    # ==========================================================================
    # Initializes the PlanarPrintOrganizer and creates PrintPoints
    # ==========================================================================
    print_organizer = ...
    ...

    # ==========================================================================
    # Set fabrication-related parameters
    # ==========================================================================
    ...
    ...
    ...
    ...

    # ==========================================================================
    # Prints out the info of the PrintOrganizer
    # ==========================================================================
    ...

    # ==========================================================================
    # Converts the PrintPoints to data and saves to JSON
    # =========================================================================
    ...
    ...

    end_time = time.time()
    print("Total elapsed time", round(end_time - start_time, 2), "seconds")


if __name__ == "__main__":
    main()
