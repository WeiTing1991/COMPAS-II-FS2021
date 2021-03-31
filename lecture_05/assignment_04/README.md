# Assignment 04

* Continuation from hands-on exercise
* Based on the work done during lecture on the example `15_pick_and_place.ghx` explore different sequences of place frames
* Store all the trajectories (pick+move+place) for at least 8 elements in a JSON file, use `compas.json_dump` to keep data type information

More about serialization: https://compas.dev/compas/latest/tutorial/serialization.html 

## How to start

Use the example file `15_pick_and_place.ghx` as starting point.

## Expected result

![Path plan](path-plan.png)

## How to submit your assignment

1. Make sure you have forked this repository already, if not, check [assignment submission instructions in lecture 02](../../lecture_02/assignment_01#how-to-submit-your-assignment).
2. Make sure your local clone is up to date on the `main` branch

       (compas-fs2021) git checkout main
       (compas-fs2021) git pull origin

3. Use a branch called `assignment-04` for this week's assignment

       (compas-fs2021) git checkout -b assignment-04
       (compas-fs2021) git push -u assignments assignment-04

4. Create a folder with your name and last name, eg. `elvis_presley` (make sure it is inside the current assignment folder)
5. Copy example `15_pick_and_place.ghx` and paste it into your folder.
6. Solve the coding assignment and commit
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
