---
title:  Code review for newbies starter pack
categories: [notes]
tags: [software,collaborative]
---

Some notes to myself and people I work with.

## Target audience:
- People who wants to do code review but have no prior experience / don't know where to start.
- You who already have some code that needs help with.
- People with limited experience with git.
- People who don't have a clear understanding with how to plan your project.
- People with a unstructured code base.
- You write "Okay", "update", "done" a lot in your commits.

## Requirements:
- A github account
- Existing code

## Instructions for people who doesn't have a clue about where to start
1. If your code is not version controlled with git, initiate your project as a git repository and commit it to github. [See full instructions here.](https://docs.github.com/en/free-pro-team@latest/github/importing-your-projects-to-github/adding-an-existing-project-to-github-using-the-command-line)
2. Create a new branch and give it a helpful name. For example `initial_review`
3. On this branch, add comments to places that you are unsure about.
4. Commit these new changes with a useful commit message. Such as "flag up sections I need help with"
5. Push this new branch to github
6. Do a pull request from `initial_review` to main. Tag your friend to let them know you are ready to comment.
7. From this point on you should be able to follow the [github code review tutorial](https://github.com/features/code-review/)

## Guides for future code review
When doing code review in this scenrio, focus on the following points:
1. How to better structure the code base
2. How to isolate redundant code into reusable functions
3. Commit changes frequently with useful commit messages. Think about how to describe the changes with some verbs suggested here:
    - fix [something]
    - update [something]
    - add [something]
    - remove [something]
    - enhance [something]
    - other useful action verbs
If you cannot, you are probably not thinking about your code in a modular way.

After the first round you should be able to find some idea to organise your code better. This means instead of updating a bunch of things in the code, the changes would focus on specific features.

## As the Reviewees
When you ask a friend to do code review, they are doing you a favour. Try to write a summary of the changes that will help your friend understand what's going on.
