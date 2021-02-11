# COMPAS II

> 064-0026-00L Introduction to Computational Methods for Digital Fabrication in Architecture

This PhD-level course introduces digital fabrication methods and tools building up on the theoretical and practical knowledge acquired in the prerequisite course. Students learn fundamentals of robotics, robot kinematics and planning, and basics of robot control applied in the domain of architecture and digital fabrication using the COMPAS framework and open source tools.

## Schedule, FS 2021

| Lecture | Date   | Session content                                                                                                                                                                                                                                                                                                                                                                                                                          | Session leads      |
|---------|--------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------|
| 01      | 24.02. | **Introduction**<br>Introduction to digital fabrication methods and the COMPAS ecosystem for digital fabrication: core, fab, rrc, slicer.<br>Brief overview of core data structures (network, mesh).<br>Remote procedure calls.                                                                                                                                                                                                          | All                |
| 02      | 03.03. | **Robotic fundamentals**<br>Introduction to robotics: anatomy of an industrial robot, coordinate systems, transformations.<br>Brief intro to kinematic functions and path planning.<br>Assignment: [TBD]                                                                                                                                                                                                                                 | GKR (RR, BL, GC)   |
| 03      | 10.03. | **Robot models**<br>Models from URDF, programmatic models.<br>Robot model visualization in Rhino / Grasshopper.<br>Forward kinematics of open chain manipulators.<br>Assignment: model your own robot.                                                                                                                                                                                                                                                              | GKR (RR, BL, GC)   |
| 04      | 17.03. | **ROS & MoveIt in the design environment**<br>Introduction to ROS, topics, services, actions. Basic interprocess communication via ROS nodes. Reproducible ROS environments with Docker.<br>Robot planning: forward and inverse kinematic  functions, analytical (closed-form) and numerical solvers. MoveIt integration from the parametric design environment.<br>[PyBullet integration (?)]<br>Assignment: [TBD, based on IK solving] | GKR (RR, BL, GC)   |
| 05      | 31.03. | **Path planning**<br>Cartesian and kinematic path planning using MoveIt.<br>Planning scene operations. End effectors and discrete build elements.<br>Assignment: [TBD]                                                                                                                                                                                                                                                                   | GKR (RR, BL, GC)   |
| 06      | 14.04. | **Assembly of discrete elements I**<br>Brief introduction to directed acyclic graphs. Modelling assembly processes as DAGs. Planning pick-and-place operations.<br>Assignment: [TBD, Ondulated brick wall?]                                                                                                                                                                                                                              | GKR (RR, BL, GC)   |
| 07      | 21.04. | **Assembly of discrete elements II**<br>Applied exercise from design to planning fabrication for an assembly of discrete elements and preparation for control exercise.                                                                                                                                                                                                                                                                  | GKR (RR, BL, GC)   |
| 08      | 28.04. | **Robot control with COMPAS RRC**<br>Online non-real time control of industrial robots. Components of an RRC deployment. Communication primitives (blocking, futures, cyclic). Instructions. Multi controller & location coordination.<br>Assignment: [TBD, Pick and place exercise]                                                                                                                                                     | GKR (RR, BL, GC)   |
| 09      | 05.05. | **Assembly of discrete elements III**<br>Continued applied exercise from planning data to robot control for an assembly of discrete elements.                                                                                                                                                                                                                                                                                            | GKR (RR, BL, GC)   |
| 10      | 12.05. | **COMPAS SLICER: Basics**<br>Introduction to COMPAS SLICER (presentation).<br>Planar slicing of simple geometry<br>Simulating and planning of robotic motion with COMPAS RRC and COMPAS SLICER<br>G-code generation?                                                                                                                                                                                                                     | DBT & GKR (IM, JB) |
| 11      | 19.05. | **COMPAS SLICER: Advanced**<br>Introduction to non-planar slicing.<br>Non-planar slicing of a geometry.<br>Simulation and planning of robotic motion with COMPAS RRC.<br>Assignment: [TBD, ideas: generation of planar g-code for a desktop 3D printer, simulation of robotic motion (planar or non-planar) using COMPAS RRC]                                                                                                            | DBT & GKR (IM, JB) |
| 12      | 26.05. | **Advancing computational research**<br>Research reproducibility and Upstreaming research output.                                                                                                                                                                                                                                                                                                                                        | GKR (RR, BL, GC)   |
| 13      | 02.06. | Closing                                                                                                                                                                                                                                                                                                                                                                                                                                  | All                |

## Information

Links:
[Course info on ETHZ Catalog](http://www.vvz.ethz.ch/Vorlesungsverzeichnis/lerneinheit.view?semkez=2021S&ansicht=ALLE&lerneinheitId=153368&lang=en) |
[Slack workspace](https://join.slack.com/t/compasii/shared_invite/zt-l9ekxyra-WdcXdBbALYtleTO3P7j1bA) |
Github Classroom

### Objectives

1. Understand fundamentals of robotics, coordinate systems, transformations and orientation representations.
1. Learn forward and inverse kinematic functions and their application.
1. Learn Cartesian and kinematic robot planning methods
1. Apply these concepts to design and implement digital fabrication processes.
1. Gain an understanding of different robot control methods and their application.
1. Learn how to generate fabrication data for a (robotic) 3D printing process using a custom slicing method.

### Content

Lectures, tutorials and project-based exercises will focus on:

* Introduction to fundamentals of robotics.
* Introduction to COMPAS framework and core extensions for digital fabrication (fab, rrc, slicer)
* Robot model representations.
* Robot forward and inverse kinematics.
* Robot path planning: Cartesian motion planning and kinematic motion planning, planning scene and collision detection.
* Integration of planning tools into parametric design environment (CAD).
* Overview and usage of ROS (Robot Operating System).
* Design of digital fabrication processes (assembly of discrete elements, 3D printing, etc.).

## Requirements

* Minimum OS: Windows 10 Pro or Mac OS Sierra 10.12
* [Anaconda 3](https://www.anaconda.com/distribution/)
* [Docker Desktop](https://www.docker.com/products/docker-desktop) Docker Toolbox would also work but it's a bit more annoying. After installation on Windows, it is required to enable "Virtualization" on the BIOS of the computer.
* [Rhino 6 & Grasshopper](https://www.rhino3d.com/download)
* [Visual Studio Code](https://code.visualstudio.com/): Any python editor works, but we recommend VS Code + extensions [as mentioned in our docs](https://gramaziokohler.github.io/compas_fab/latest/getting_started.html#working-in-visual-studio-code-1)

## Installation

> **TODO**: Add compas_slicer and compas_rrc to installation

We use `conda` to make sure we have clean, isolated environment for dependencies.

First time using `conda`? Make sure you run this at least once:

    (base) conda config --add channels conda-forge

Create a new conda environment in one of two ways.  Manually:

**Windows**

    (base) conda create -n compas-fs2021 python=3.8 compas_fab=0.16 --yes
    (base) conda activate compas-fs2021

**Mac**

    (base) conda create -n compas-fs2021 python=3.8 compas_fab=0.16 python.app --yes
    (base) conda activate compas-fs2021
    
Or, after cloning this repository:

    (base) conda env create -f path/to/COMPAS-II-FS2021/environment.yml

### Verify installation

    (compas-fs2021) pip show compas_fab
    Name: compas-fab
    Version: 0.16.0
    Summary: Robotic fabrication package for the COMPAS Framework
    ...


### Install on Rhino

    (compas-fs2021) python -m compas_rhino.install

NOTE: This installs to Rhino 6.0, use `-v 5.0` if needed.
