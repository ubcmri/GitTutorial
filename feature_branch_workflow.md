# The Feature Branch Workflow

## Introduction
This short document outlines the workflow that we propose to use in the group as we slowly start to use Github more and more. The workflow presented here is not novel and has been described in many other places before. Here I have picked up most of the information from the Atlassian git tutorial that can be found on the link below:
https://www.atlassian.com/git/tutorials/comparing-workflows/feature-branch-workflow

## Branch and merge structure
- Implementation of new features are done by starting a new branch that is pushed to the central repository on Github, allowing other users to take part of the work and development process.
- Branches are required to have a descriptive name to give a clear idea of the work that is being made on that branch. We will try to adhere to the following guidelines:
    - New features: feat-<description>
    - Bug fix: fix-<description>
    - Other: misc-<description>
- Once development is finished on a branch, a pull request is made to merge the feature branch on to the master branch. The merge is completed by the repository administrator.
- After a feature branch is successfully merged into master it is deleted

## Issue Tracking
- Although this is not a part of the official workflow, it will be very useful for us to keep track of our work using the issue tracking system which is a part of Github.
- This can be used in a few different ways:
    - You have found a bug and you want to fix it. You create a new issue to let other people know you are working on it, assign yourself to the issue and get to work.
    - You have found a bug but don't have time to fix it: Create an issue and describe what you think is required to fix it. Keep your fingers crossed that someone will fix it.
    - You have time to kill so you browse the issues and find something you can help out with: Assign yourself to the issue, see if there is a branch created for the issue. If so, check out that branch, if not, create one and get to work!
