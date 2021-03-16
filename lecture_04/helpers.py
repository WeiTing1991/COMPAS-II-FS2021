import math
from compas_fab.robots import Configuration

def show_trajectory(trajectory):
    import matplotlib.pyplot as plt
    # visualise
    positions = []
    velocities = []
    accelerations = []
    time_from_start = []

    for p in trajectory.points:
        positions.append(p.positions)
        velocities.append(p.velocities)
        accelerations.append(p.accelerations)
        time_from_start.append(p.time_from_start.seconds)

    plt.rcParams['figure.figsize'] = [17, 4]
    plt.subplot(131)
    plt.title('positions')
    plt.plot(positions)
    plt.subplot(132)
    plt.plot(velocities)
    plt.title('velocities')
    plt.subplot(133)
    plt.plot(accelerations)
    plt.title('accelerations')
    plt.show()


def plan_picking_motion(robot, picking_frame, safelevel_picking_frame, start_configuration, attached_element_mesh):
    """Returns a cartesian trajectory to pick an element.

    Parameters
    ----------
    robot : :class:`compas.robots.Robot`
    picking_frame : :class:`Frame`
    safelevel_picking_frame : :class:`Frame`
    start_configuration : :class:`Configuration`
    attached_element_mesh : :class:`AttachedCollisionMesh`

    Returns
    -------
    :class:`JointTrajectory`
    """

    # Calculate frames at tool0 and picking_configuration
    frames = [picking_frame, safelevel_picking_frame]
    frames_tool0 = robot.from_tcf_to_t0cf(frames)

    picking_frame_tool0 = robot.from_tcf_to_t0cf([picking_frame])[0]
    picking_configuration = robot.inverse_kinematics(picking_frame_tool0, start_configuration)

    picking_trajectory = robot.plan_cartesian_motion(frames_tool0,
                                                     picking_configuration,
                                                     options=dict(
                                                        max_step=0.01,
                                                        attached_collision_meshes=[attached_element_mesh]
                                                     ))
    return picking_trajectory



def plan_moving_and_placing_motion(robot, element, start_configuration, tolerance_vector, safelevel_vector, attached_element_mesh):
    """Returns two trajectories for moving and placing an element.

    Parameters
    ----------
    robot : :class:`compas.robots.Robot`
    element : :class:`Element`
    start_configuration : :class:`Configuration`
    tolerance_vector : :class:`Vector`
    safelevel_vector : :class:`Vector`
    attached_element_mesh : :class:`AttachedCollisionMesh`

    Returns
    -------
    list of :class:`JointTrajectory`
    """

    tolerance_position = 0.001
    tolerance_axes = [math.radians(1)] * 3

    target_frame = element._tool_frame.copy()
    target_frame.point += tolerance_vector

    safelevel_target_frame = target_frame.copy()
    safelevel_target_frame.point += safelevel_vector

    # Calculate goal constraints
    safelevel_target_frame_tool0 = robot.from_tcf_to_t0cf(
        [safelevel_target_frame])[0]
    goal_constraints = robot.constraints_from_frame(safelevel_target_frame_tool0,
                                                    tolerance_position,
                                                    tolerance_axes)

    moving_trajectory = robot.plan_motion(goal_constraints,
                                          start_configuration,
                                          options=dict(
                                            planner_id='SBL',
                                            attached_collision_meshes=[attached_element_mesh],
                                            num_planning_attempts=20,
                                            allowed_planning_time=10
                                          ))


    frames = [safelevel_target_frame, target_frame]
    frames_tool0 = robot.from_tcf_to_t0cf(frames)
    # as start configuration take last trajectory's end configuration
    last_configuration = Configuration(moving_trajectory.points[-1].values, moving_trajectory.points[-1].types)


    placing_trajectory = robot.plan_cartesian_motion(frames_tool0,
                                                     last_configuration,
                                                     options=dict(
                                                        max_step=0.01,
                                                        attached_collision_meshes=[attached_element_mesh]
                                                     ))
    return moving_trajectory, placing_trajectory


class _Getch:
    """Gets a single character from standard input.  Does not echo to the
screen."""
    def __init__(self):
        try:
            self.impl = _GetchWindows()
        except ImportError:
            self.impl = _GetchUnix()

    def __call__(self): return self.impl()


class _GetchUnix:
    def __init__(self):
        import tty, sys

    def __call__(self):
        import sys, tty, termios
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch


class _GetchWindows:
    def __init__(self):
        import msvcrt

    def __call__(self):
        import msvcrt
        return msvcrt.getch()


getch = _Getch()

CTRL_CHARS = (8, 9, 13, 27)
__input_context = dict(buffer='')

def get_current_buffer():
    return __input_context['buffer']

def get_input(prompt='> ', end='\n'):
    if prompt:
        print(prompt, end='', flush=True)

    __input_context['buffer'] = ''
    while True:
        c = getch()
        ord_c = ord(c)
        if ord_c in CTRL_CHARS:
            if ord_c == 13:
                # only break if text has content
                if len(__input_context['buffer']) > 0: break
            elif ord_c == 8:
                # only apply backspace if text has content
                if len(__input_context['buffer']) > 0:
                    c = c.decode('ascii')
                    print(c + ' ' + c, end='', flush=True)
                    __input_context['buffer'] = __input_context['buffer'][:-1]
        else:
            c = c.decode('ascii')
            print(c, end='', flush=True)
            __input_context['buffer'] += c

    if end:
        print(end, end='', flush=True)

    return __input_context['buffer']
