# COMPAS II

> 064-0026-00L Introduction to Computational Methods for Digital Fabrication in Architecture

This PhD-level course introduces digital fabrication methods and tools building up on the theoretical and practical knowledge acquired in the prerequisite course. Students learn fundamentals of robotics, robot kinematics and planning, and basics of robot control applied in the domain of architecture and digital fabrication using the COMPAS framework and open source tools.

## Schedule, FS 2021

| Lecture | Date   | Session content                                                                                                                                                                                                                                                                                                                                                                                                                          | Session leads      |
|---------|--------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------|
| 01      | 24.02. | **Introduction**<br>Introduction to digital fabrication methods and the COMPAS ecosystem for digital fabrication: core, fab, rrc, slicer.<br>Brief overview of core data structures (network, mesh).<br>Remote procedure calls.<br>👉[Go to lecture](lecture_01/README.md)                                                                                                                                                               | All                |
| 02      | 03.03. | **Robotic fundamentals**<br>Introduction to robotics: anatomy of an industrial robot, coordinate systems, transformations.<br>Brief intro to kinematic functions and path planning.<br>👉[Go to lecture](lecture_02/README.md)                                                                                                                                                                                                           | GKR (RR, BL, GC)   |
| 03      | 10.03. | **Robot models**<br>Models from URDF, programmatic models.<br>Robot model visualization in Rhino / Grasshopper.<br>Forward kinematics of open chain manipulators.<br>Assignment: model your own robot.<br>👉[Go to lecture](lecture_03/README.md)                                                                                                                                                                                        | GKR (RR, BL, GC)   |
| 04      | 17.03. | **ROS & MoveIt in the design environment**<br>Introduction to ROS, topics, services, actions. Basic interprocess communication via ROS nodes. Reproducible ROS environments with Docker.<br>Robot planning: forward and inverse kinematic  functions, analytical (closed-form) and numerical solvers. MoveIt integration from the parametric design environment. Assignment: IK with MoveIt<br>👉[Go to lecture](lecture_04/README.md)   | GKR (RR, BL, GC)   |
| 05      | 31.03. | **Path planning**<br>Cartesian and kinematic path planning using MoveIt.<br>Planning scene operations. End effectors and discrete build elements.<br>👉[Go to lecture](lecture_05/README.md)                                                                                                                                                                                                                                             | GKR (RR, BL, GC)   |
| 06      | 14.04. | **Assembly of discrete elements I**<br>Brief introduction to directed acyclic graphs. Modelling assembly processes as DAGs. Planning pick-and-place operations.<br>👉[Go to lecture](lecture_06/README.md)                                                                                                                                                                                                                               | GKR (RR, BL, GC)   |
| 07      | 21.04. | **Assembly of discrete elements II**<br>Applied exercise from design to planning fabrication for an assembly of discrete elements and preparation for control exercise.<br>👉[Go to lecture](lecture_07/README.md)                                                                                                                                                                                                                       | GKR (RR, BL, GC)   |
| 08      | 28.04. | **Robot control with COMPAS RRC**<br>Online non-real time control of industrial robots. Components of an RRC deployment. Communication primitives (blocking, futures, cyclic). Instructions. Multi controller & location coordination.<br>👉[Go to lecture](lecture_08/README.md)                                                                                                                                                        | GKR (RR, BL, GC)   |
| 09      | 05.05. | **Assembly of discrete elements III**<br>Continued applied exercise from planning data to robot control for an assembly of discrete elements.<br>👉[Go to lecture](lecture_09/README.md)                                                                                                                                                                                                                                                 | GKR (RR, BL, GC)   |
| 10      | 12.05. | **COMPAS SLICER: Basics**<br>Introduction to COMPAS SLICER (presentation).<br>Planar slicing of simple geometry<br>Introducion to scalar field slicing.<br>👉[Go to lecture](lecture_10/README.md)                                                                                                                                                                                                                                       | DBT & GKR (IM, JB) |
| 11      | 19.05. | **COMPAS SLICER: Advanced**<br>Introduction to non-planar slicing.<br>Non-planar slicing of a geometry.<br>Simulation and planning of robotic motion with COMPAS RRC.<br>👉[Go to lecture](lecture_11/README.md)                                                                                                                                                                                                                         | DBT & GKR (IM, JB) |
| 12      | 26.05. | **Advancing computational research**<br>Research reproducibility and Upstreaming research output.<br>👉[Go to lecture](lecture_12/README.md)                                                                                                                                                                                                                                                                                             | GKR (RR, BL, GC)   |
| 13      | 02.06. | Closing                                                                                                                                                                                                                                                                                                                                                                                                                                   | All                |

## Information

Links:
[Course info on ETHZ Catalog](http://www.vvz.ethz.ch/Vorlesungsverzeichnis/lerneinheit.view?semkez=2021S&ansicht=ALLE&lerneinheitId=153368&lang=en) |
[Slack workspace](https://join.slack.com/t/compasii/shared_invite/zt-mi3kyo2f-aMdyGCKubeTfKnKPdczpcQ) |
[COMPAS docs](https://compas.dev)

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
* [Rhino 6/7 & Grasshopper](https://www.rhino3d.com/download)
* [Visual Studio Code](https://code.visualstudio.com/): Any python editor works, but we recommend VS Code + extensions [as mentioned in our docs](https://gramaziokohler.github.io/compas_fab/latest/getting_started.html#working-in-visual-studio-code-1)

## Installation

We use `conda` to make sure we have clean, isolated environment for dependencies.

First time using `conda`? Make sure you run this at least once:

    (base) conda config --add channels conda-forge

Clone this repository and create a new conda environment:

    (base) cd path/to/COMPAS-II-FS2021
    (base) conda env create -f environment.yml
    (base) conda activate compas-fs2021

<details><summary>Alternatively, create environment manually</summary>
<p>

The conda environment can also be manually created:

    (base) conda create -n compas-fs2021 python=3.8 compas_fab>=0.16 --yes
    (base) conda activate compas-fs2021

</p>
</details>

**Mac**

Also install `python.app` after activating the environment:

    (compas-fs2021) conda install python.app

### Verify installation

    (compas-fs2021) python -m compas

    Yay! COMPAS is installed correctly!

    COMPAS: 1.1.0
    Python: 3.8.8 | packaged by conda-forge | (default, Feb 20 2021, 15:50:08) [MSC v.1916 64 bit (AMD64)]
    Extensions: ['compas-cgal', 'compas-fab', 'compas-slicer']

### Install on Rhino

    (compas-fs2021) python -m compas_rhino.install
    (compas-fs2021) python -m compas_rhino.install -v 7.0

### Update installation

To update your environment:

    (compas-fs2021) conda env update -f environment.yml
