# COMPAS II: ROS & MoveIt in the design environment

Introduction to ROS, topics, services, actions.

Basic inter-process communication via ROS nodes. Reproducible ROS environments with Docker.

Robot planning: forward and inverse kinematic functions, analytical and numerical solvers. MoveIt integration from the parametric design environment.

👉 [Slides](lecture_04.pdf)
📜 [Assignment 03](assignment_03/README.md)

## Examples

* ROS Basics
  * [Verify connection](01_check_connection.py)
  * [Interconnected nodes: Talker](02_ros_hello_world_talker.py)
  * [Interconnected nodes: Listener](03_ros_hello_world_listener.py)
  * [Interconnected nodes across the Internet: Chat](04_ros_chat.py)

* ROS & MoveIt planning with UR5
  * [Load robot](05_robot_from_ros.py)
  * [Load robot in Rhino](06_robot_from_ros_rhino.py)
  * [Forward Kinematics](07_forward_kinematics_ros_loader.py)
  * [Inverse Kinematics](08_inverse_kinematics_ros_loader.py)
  * [Cartesian motion planning](09_plan_cartesian_motion_ros_loader.py)
  * [Cartesian motion planning + graphs](10_plan_cartesian_motion_ros_loader_viz.py)
  * [Free space motion planning](11_plan_motion_ros_loader.py)
  * [Free space motion planning + graphs](12_plan_motion_ros_loader_viz.py)

* Planning scene in MoveIt
  * [Add objects to the scene](13_add_collision_mesh.py)
  * [Append nested objects to the scene](14_append_collision_meshes.py)
  * [Remove objects from the scene](15_remove_collision_mesh.py)

* MoveIt & Grasshopper
  * [Robot in Grasshopper](16_robot_example.ghx)
