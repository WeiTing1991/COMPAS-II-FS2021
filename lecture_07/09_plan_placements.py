import math
import os

import helpers
from compas_fab.backends import RosClient
from compas_fab.robots import PlanningScene

import compas
from compas.geometry import Translation

HERE = os.path.dirname(__file__)
MAX_STEP = 0.01

# Load assembly
filename = os.path.join(HERE, 'assembly.json')
assembly = compas.json_load(filename)

with RosClient() as client:
    robot = client.load_robot()
    scene = PlanningScene(robot)

    # Prepare scene for planning
    helpers.attach_vacuum_gripper(scene)
    helpers.add_static_objects(scene)

    # Get sequence
    assembly_sequence = helpers.traversal_linearly_ordered(assembly)
    print('Sequence: {}'.format(assembly_sequence))

    built = []
    for key in assembly_sequence:
        e = assembly.element(key)
        if e.trajectory:
            print('Skipping already planned element {}'.format(key))
            continue

        print('Planning element {}:'.format(key))
        print('  - Preparing scene: ', end='')

        # Add built elements to the scene
        helpers.add_built_elements(scene, assembly, built)
        print()

        place_t0cf_frame, approach_t0cf_frame = robot.from_tcf_to_t0cf([e.frame, e.approach_frame])

        # Apply place tolerance
        x, y, z = 0, 0, assembly.attributes['place_tolerance']
        place_t0cf_frame = place_t0cf_frame.transformed(Translation.from_vector([x, y, z]))

        tolerance_position = 0.001
        tolerance_axes = [math.radians(1)] * 3

        # create goal constraints from frame
        goal_constraints = robot.constraints_from_frame(approach_t0cf_frame,
                                                        tolerance_position,
                                                        tolerance_axes)

        # get start configuration
        start_configuration = helpers.get_last_config(assembly.pick_trajectory, robot)

        print('  - Planning kinematic motion: ', end='', flush=True)
        trajectory = robot.plan_motion(goal_constraints,
                                       start_configuration,
                                       options=dict(planner_id='RRTstarkConfigDefault'))
        print('OK ({} points)'.format(len(trajectory.points)))

        # Plan cartesian insertion
        print('  - Planning cartesian insertion: ', end='', flush=True)
        frames = [approach_t0cf_frame, place_t0cf_frame]
        start_configuration = helpers.get_last_config(trajectory, robot)

        place_trajectory = robot.plan_cartesian_motion(frames,
                                                       start_configuration,
                                                       options=dict(
                                                           max_step=MAX_STEP,
                                                           avoid_collisions=True,
                                                       ))

        if place_trajectory and place_trajectory.fraction < 1.0:
            raise Exception('Incomplete trajectory. Fraction={}'.format(place_trajectory.fraction))

        print('OK ({} points)'.format(len(place_trajectory.points)))

        # Merge and store
        e.trajectory = trajectory.points + place_trajectory.points

        built.append(key)

        # if len(built) == 3:
        #     break

        # Save assembly
        compas.json_dump(assembly, filename)
