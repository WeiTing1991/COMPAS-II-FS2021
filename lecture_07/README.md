# COMPAS II: Assembly of discrete elements II

Applied exercise from design to planning fabrication for an assembly of discrete elements and preparation for control exercise.

👉 [Slides](lecture_07.pdf)

## Examples

Make sure you start (`compose up`) the container with a UR5 planner for these examples. You can use
either [the one with browser-based UI](../docker/moveit/docker-compose.yml) or
the [lightweight version of it without UI](../docker/ur5-planner/docker-compose.yml).

* Sequence assignments
  * [Default sequence](01_assign_default_sequence.py)
  * [Linear sorted sequence](02_assign_linear_sequence.py)

* Planning
  * [Plan pick trajectory](08_plan_pick_trajectory.py)
  * [Plan all brick placements](09_plan_placements.py)

* Assembly visualizations
  * [Grasshopper viewer](20_assembly_viewer.ghx)
  * [Connectivity viewer in Rhino](21_assembly_connectivity_rhino.py)

* Clear data
  * [Clear planning scene](10_clear_planning_scene.py)
  * [Clear all trajectories](11_clear_all_trajectories.py)
