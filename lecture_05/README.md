# COMPAS II: Path planning

Cartesian and kinematic path planning using MoveIt.

Planning scene operations.

End effectors.

Method for Pick and Place planning.

👉 [Slides](lecture_05.pdf)
📜 [Assignment 04](assignment_04/README.md)

## Examples

Make sure you start (`compose up`) the container with a UR5 planner for these examples. You can use
either [the one with browser-based UI](../docker/moveit/docker-compose.yml) or
the [lightweight version of it without UI]((../docker/ur5-planner/docker-compose.yml)).

* Path planning with MoveIt
  * [Cartesian motion planning](01_plan_cartesian_motion_ros_loader.py)
  * [Cartesian motion planning + graphs](02_plan_cartesian_motion_ros_loader_viz.py)
  * [Free space motion planning](03_plan_motion_ros_loader.py)
  * [Free space motion planning + graphs](04_plan_motion_ros_loader_viz.py)
  * [Constraints](05_constraints.py)

* Planning scene in MoveIt
  * [Add objects to the scene](07_add_collision_mesh.py)
  * [Append nested objects to the scene](08_append_collision_meshes.py)
  * [Remove objects from the scene](09_remove_collision_mesh.py)

* Pick and place process
  * [Attach tool](10_attach_tool.py)
  * [Detach tool](11_detach_tool.py)
  * [Plan cartesian motion with tool](12_plan_cartesian_motion_with_attached_tool.py)

* Hands-on exercise
  * [Pick and Place planning](15_pick_and_place.ghx)
