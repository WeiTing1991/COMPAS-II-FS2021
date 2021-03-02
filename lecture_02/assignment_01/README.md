# Assignment 01

Project box to xy-plane:

* Create a box at a certain location with a certain orientation.
* Create a Projection (can be orthogonal, parallel or perspective)
* Convert the box to a mesh and project the it onto the xy-plane.
* Use artists to draw the result

## Helpful links

* [Documentation of `Projection`](https://compas.dev/compas/latest/api/generated/compas.geometry.Projection.html?highlight=projection#compas.geometry.Projection)

## Expected result

![The result](project_box.jpg)

## How to submit your assignment

1. Fork this repository

    ![How to fork a repo](../../.github/fork.png)

2. Add a new remote (<small>[What's a remote?](https://docs.github.com/en/github/using-git/about-remote-repositories)</small>)

        (compas-fs2021) cd path/to/COMPAS-II-FS2021
        (compas-fs2021) git remote add assignments https://github.com/REPLACE_THIS_WITH_YOUR_GITHUB_USERNAME/COMPAS-II-FS2021

3. Use a branch called `assignment-01` for this week's assignment

        (compas-fs2021) git checkout -b assignment-01
        (compas-fs2021) git push -u assignments assignment-01

4. Copy the folder `name_lastname` and rename accordingly with your details, eg. `elvis_presley`
5. Solve the coding assignment in the `assignment_*.py` files and commit
6. Once you're ready to submit, push the changes:

        git push assignments

7. And create a pull request (<small>[What's a pull request?](https://docs.github.com/en/github/collaborating-with-issues-and-pull-requests/about-pull-requests)</small>)

    1. Open your browser and go to your fork
    2. Create the pull request clicking `Compare & pull request` and follow the instructions

    ![Start a pull request](../../.github/pull-request.png)
