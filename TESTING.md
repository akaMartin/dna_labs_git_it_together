# Testing Guide

This document contains scenarios you can use to practice git commands.

## Scenario 1: Basic Workflow

1. Add a new function to `utils.py` to sort todos
2. Stage and commit this change
3. View your commit with `git show`

## Scenario 2: Branching

1. Create a new branch called `feature/save-load`
2. Implement save/load functionality in `main.py`
3. Commit your changes
4. Switch back to main
5. Merge your feature branch

## Scenario 3: Undoing Changes

1. Make a change you don't like in `todo.py`
2. Use `git checkout -- todo.py` to discard it
3. Make a commit on main
4. Use `git revert` to undo that commit

## Scenario 4: Multiple Branches

1. Create branch `feature/filter` - add ability to filter todos
2. Create branch `bugfix/description` - fix description display
3. Work on both branches
4. Merge them both into main

## Scenario 5: Resolving Conflicts

1. Create branch `feature/priority`
2. Add priority field in `todo.py` on this branch
3. On main, modify `todo.py` in a conflicting way
4. Merge the feature branch and resolve conflicts

