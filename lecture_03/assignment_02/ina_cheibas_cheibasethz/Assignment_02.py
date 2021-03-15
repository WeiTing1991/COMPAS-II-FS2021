# * Build your own robot with a certain number n of links and n - 1 configurable joints.
# * Create a `Configuration` with certain values and the correct joint types.
# * Create a `RobotModelArtist`  of your preference (e.g. `compas_ghpython` or `compas_rhino`)
# * Use the artist to update the robot with the created configuration (using its `joint_dict`), such that it configures into the letter of your choice (or any other identifiable figure).

"""Assignment 02: Build your own robot model
"""
# Rhino
from compas_fab.robots import Configuration
from compas_rhino.artists import RobotModelArtist
from compas_rhino.artists import CylinderArtist, SphereArtist
from compas.datastructures import Mesh
from compas.geometry import Circle, Cylinder, Sphere
from compas.geometry import Point
from compas.geometry import Plane, Frame
from compas.geometry import Translation, Rotation
from compas.robots import Joint
from compas.robots import RobotModel

# create sphere in yz plane
p = 6
rad1 = 6
sphere1 = Sphere(Point(p, p, p), rad1)
rad2 = 3
sphere2 = Sphere(Point(p, p, p + rad2), rad2)
sphere2.transform(Translation.from_vector([0, 0, rad1]))
radius, length = 5, 1
cylinder = Cylinder(Circle(Plane([0, 0, 0], [1, 0, 0]), radius), length)
cylinder.transform(Rotation.from_basis_vectors([0, 0, 1], [0, 1, 0]))
cylinder.transform(Translation.from_vector([p, p, p * 3]))

#artist1 = CylinderArtist(cylinder, color=(0.3,0.2,0.4))
#artist1.draw()
#artist2 = SphereArtist(sphere1, color=(0.3,0.2,0.4))
#artist2.draw()
#artist3 = SphereArtist(sphere2, color=(0.3,0.2,0.4))
#artist3.draw()

# create robot
model = RobotModel("insectface", links=[], joints=[])

# add links and joints to the robot model
link0 = model.add_link("world")

# add second link to robot
mesh = Mesh.from_shape(sphere1)
link1 = model.add_link("link1", visual_mesh=mesh, visual_color=(0.2, 0.5, 0.6))
# add the joint between the links
axis = (0, 0, 1)
origin = Frame.worldXY()
model.add_joint("joint1", Joint.CONTINUOUS, link0, link1, origin, axis)


# add third link
mesh = Mesh.from_shape(sphere2)  # create a copy!
link2 = model.add_link("link2", visual_mesh=mesh, visual_color=(0.4, 0.6, 0.2))
# add second joint to 'glue' the link to the chain
origin = Frame((0, 0, 0), (0, 1, 0), (0, 0, 1))
model.add_joint("joint2", Joint.CONTINUOUS, link1, link2, origin, axis)

# add forth link
mesh = Mesh.from_shape(cylinder)  # create a copy!
link3 = model.add_link("link3", visual_mesh=mesh, visual_color=(0.5, 0.2, 0.2))
# add third joint to the chain
origin = Frame((0, 0, 0), (1, 0, 0), (0, 1, 0))
model.add_joint("joint3", Joint.CONTINUOUS, link2, link3, origin, axis)

# Update the model using the artist
artist = RobotModelArtist(model,layer='COMPAS::insectface')
artist.clear_layer()
for i in range(100):
    # Create a configuration object matching the number of joints in your model
    configuration = Configuration.from_revolute_values([i, i*2, i*3], ["joint1", "joint2", "joint3"])

    artist.update(configuration.joint_dict)
    # Render everything
    artist.draw_visual()
    artist.redraw()


# ## Helpful links

# * [Documentation of `RobotModelArtist`](https://compas.dev/compas/latest/api/generated/compas_rhino.artists.RobotModelArtist.html)
# * [Robot model tutorial](https://compas.dev/compas/latest/tutorial/robots.html#)

# ## Expected result

# > NOTE: It should be some recognizable shape, but not necessarily a letter M as in this image!

# ![The result](robot_model.jpg)

# ## How to submit your assignment

# 1. You should have forked this repository last week, if not, check assignment submission of last week's lecture.
# 2. Make sure your local clone is up to date

#        (compas-fs2021) git checkout main
#        (compas-fs2021) git pull origin

# 3. Use a branch called `assignment-02` for this week's assignment

#        (compas-fs2021) git checkout -b assignment-02
#        (compas-fs2021) git push -u assignments assignment-02

# 4. Create a folder with your name and last name, eg. `elvis_presley` (make sure it is inside the current assignment folder)
# 5. Create a Python file (eg. `assignment_02.py`) and paste the starting point code.
# 6. Solve the coding assignment and commit
#     <details><summary><small>(How do I commit?)</small></summary>
#     <p>

#     Usually, commits are done from a visual client or VS code,
#     but you can also commit your changes from the command line:

#        (compas-fs2021) git add lecture_02/assignment_02/elvis_presley/\* && git commit -m "hello world"


#     </p>
#     </details>

# 8. Once you're ready to submit, push the changes:

#        (compas-fs2021) git push assignments

# 9. And create a pull request (<small>[What's a pull request?](https://docs.github.com/en/github/collaborating-with-issues-and-pull-requests/about-pull-requests)</small>)

#     1. Open your browser and go to your fork
#     2. Create the pull request clicking `Compare & pull request` and follow the instructions

#     ![Start a pull request](../../.github/pull-request.png)
