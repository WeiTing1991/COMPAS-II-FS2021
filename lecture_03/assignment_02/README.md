# Assignment 02

Build your own robot model.

* Build your own robot with a certain number n of links and n - 1 configurable joints.
* Create a `Configuration` with certain values and the correct joint types.
* Create a `RobotModelArtist`  of your preference (e.g. `compas_ghpython` or `compas_rhino`)
* Use the artist to update the robot with the created configuration (using its `joint_dict`), such that it configures into the letter of your choice (or any other identifiable figure).

## How to start

Use the following code as a starting point for your assignment:

```python
"""Assignment 02: Build your own robot model
"""
# Rhino
from compas_fab.robots import Configuration
from compas_rhino.artists import RobotModelArtist

from compas.datastructures import Mesh
from compas.geometry import Circle
from compas.geometry import Cylinder
from compas.geometry import Frame
from compas.geometry import Plane
from compas.geometry import Translation
from compas.robots import Joint
from compas.robots import RobotModel

# create cylinder in yz plane
radius, length = 0.3, 5
cylinder = Cylinder(Circle(Plane([0, 0, 0], [1, 0, 0]), radius), length)
cylinder.transform(Translation.from_vector([length / 2., 0, 0]))

# create robot
model = RobotModel("robot", links=[], joints=[])

# add links and joints to the robot model
# link0 = model.add_link(..)
# link1 = model.add_link(..)
# joint1 = model.add_joint(..)

# Create a configuration object matching the number of joints in your model
# configuration = ....

# Update the model using the artist
artist = RobotModelArtist(model)
# artist.update ...

# Render everything
artist.draw_visual()
artist.redraw()
```

## Helpful links

* [Documentation of `RobotModelArtist`](https://compas.dev/compas/latest/api/generated/compas.geometry.Projection.html?highlight=projection#compas.geometry.Projection)

## Expected result

![The result](robot_model.jpg)

## How to submit your assignment

1. You should have forked this repository last week, if not, check assignment submission of last week's lecture.
2. Make sure your local clone is up to date

       (compas-fs2021) git checkout main
       (compas-fs2021) git pull origin

3. Use a branch called `assignment-02` for this week's assignment

       (compas-fs2021) git checkout -b assignment-02
       (compas-fs2021) git push -u assignments assignment-02

4. Create a folder with your name and last name, eg. `elvis_presley` (make sure it is inside the current assignment folder)
5. Create a Python file (eg. `assignment_02.py`) and paste the starting point code.
6. Solve the coding assignment and commit
    <details><summary><small>(How do I commit?)</small></summary>
    <p>

    Usually, commits are done from a visual client or VS code,
    but you can also commit your changes from the command line:

       (compas-fs2021) git add lecture_02/assignment_02/elvis_presley/\* && git commit -m "hello world"

    
    </p>
    </details>

8. Once you're ready to submit, push the changes:

       (compas-fs2021) git push assignments

9. And create a pull request (<small>[What's a pull request?](https://docs.github.com/en/github/collaborating-with-issues-and-pull-requests/about-pull-requests)</small>)

    1. Open your browser and go to your fork
    2. Create the pull request clicking `Compare & pull request` and follow the instructions

    ![Start a pull request](../../.github/pull-request.png)
