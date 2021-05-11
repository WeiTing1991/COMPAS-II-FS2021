# Assignment 06

Building up on the concepts that were presented in class, we will slice a model using the scalar field slicing method. In this assignment you will pick a shape of your choice (keep it simple!) and design a scalar field that will be used to slice the model and produce paths. 

For the selection of shape, we recommend a __triangulated__ and __welded__ obj or stl mesh that consist of a single shell.  

## How to start

Create a python script for slicing, and a 'data' folder that contains the mesh you want to slice.

Use the tutorial `2_scalar_field_slicing` as starting point.

## Expected result

* Code of sliced model
* Screenshot showing the result visualized in grasshopper
* A couple of sentences explaining the idea behing the design of the scalar field

## How to submit your assignment

1. Make sure you have forked this repository already, if not, check [assignment submission instructions in lecture 02](../../lecture_02/assignment_01#how-to-submit-your-assignment).
2. Make sure your local clone is up to date on the `main` branch

       (compas-fs2021) git checkout main
       (compas-fs2021) git pull origin

3. Use a branch called `assignment-06` for this week's assignment

       (compas-fs2021) git checkout -b assignment-06
       (compas-fs2021) git push -u assignments assignment-06

4. Create a folder with your name and last name, eg. `elvis_presley` (make sure it is inside the current assignment folder)
5. Work on the assignment into your folder.
6. Commit
    <details><summary><small>(How do I commit?)</small></summary>
    <p>

    Usually, commits are done from a visual client or VS code,
    but you can also commit your changes from the command line:

       (compas-fs2021) git add lecture_05/assignment_04/elvis_presley/\* && git commit -m "hello world"

    
    </p>
    </details>

8. Once you're ready to submit, push the changes:

       (compas-fs2021) git push assignments

9. And create a pull request (<small>[What's a pull request?](https://docs.github.com/en/github/collaborating-with-issues-and-pull-requests/about-pull-requests)</small>)

    1. Open your browser and go to your fork
    2. Create the pull request clicking `Compare & pull request` and follow the instructions

    ![Start a pull request](../../.github/pull-request.png)