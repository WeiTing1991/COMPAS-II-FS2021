# COMPAS II: ROS & MoveIt in the design environment

Introduction to ROS, topics, services, actions.

Basic inter-process communication via ROS nodes. Reproducible ROS environments with Docker.

Robot planning: forward and inverse kinematic functions, analytical and numerical solvers. MoveIt integration from the parametric design environment.


## Examples

* ROS Basics
  * [Verify connection](01_check_connection.py)
  * [Interconnected nodes: Talker](02_ros_hello_world_talker.py)
  * [Interconnected nodes: Listener](03_ros_hello_world_listener.py)

* ROS & MoveIt planning with UR5
  * [Forward Kinematics](04_forward_kinematics_ros_loader.py)
  * [Inverse Kinematics](05_inverse_kinematics_ros_loader.py)
  * [Cartesian motion planning](06_plan_cartesian_motion_ros_loader.py)
  * [Cartesian motion planning + graphs](07_plan_cartesian_motion_ros_loader_viz.py)
  * [Free space motion planning](08_plan_motion_ros_loader.py)
  * [Free space motion planning + graphs](09_plan_motion_ros_loader_viz.py)

* Planning scene in MoveIt
  * [Add objects to the scene](10_add_collision_mesh.py)
  * [Append nested objects to the scene](11_append_collision_meshes.py)
  * [Remove objects from the scene](12_remove_collision_mesh.py)
