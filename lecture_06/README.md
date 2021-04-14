# COMPAS II: Assembly of discrete elements I

Brief introduction to graphs and other mythical beasts.

Modelling assembly processes as DAGs.

Planning pick-and-place operations.

👉 [Slides](lecture_06.pdf)
📜 [Assignment 05](assignment_05/README.md)

## Examples

Make sure you start (`compose up`) the container with a UR5 planner for these examples. You can use
either [the one with browser-based UI](../docker/moveit/docker-compose.yml) or
the [lightweight version of it without UI](../docker/ur5-planner/docker-compose.yml).

* Graphs and other mythical beasts
  * [Linear order](01_linear_order.py)
  * [Color-mixing lattice](02_color_mixing_lattice.py)
  * [Color-mixing lattice in Rhino](03_color_mixing_lattice_rhino.py)
  * [Partial order](04_partial_order.py)
  * [Network concepts](05_network_concepts.py)
  * [Using NetworkX](06_networkx.py)

* Assembly models
  * [Basic model of a network-based assembly class](assembly.py)

* Assembly exercise
  * [Pick and Place planning as a network](07_pick_and_place_graph.ghx)
