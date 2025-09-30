---
layout: refactoring
title: Split Loop
source: Emily Bache
source_url: https://refactoring.com/catalog/splitLoop.html
code_smells: loops,divergent_change,shotgun_surgery
learning_hours: split_loop
---

# Split Loop
This is one of the refactorings in Martin Fowler's book. Often this refactoring opens up for a lot of other useful changes.

## Examine
A loop is of itself a code smell, but even more so when it does more than one thing, which implies Diverent Change.

## Prepare
Identify the loop you want to split, and in particular which lines within it that hang together and need to be separated from the others. You may need to do some 'introduce variable' refactorings and 'slide statement' refactorings to gather all the relevant parts of the loop together.

## Implement

* Tests all passing
* Select the whole loop and duplicate it.
* In the second copy of the loop, delete _everything except_ the lines you want to split.
* In the first copy of the loop, delete _only_ the lines you want to split.
* Tests all passing.

## Clear
Double-check the remaining logic in the original loop makes sense and that you didn't delete too much by mistake.

## Follow up
Often you now want to extract a method for the new loop, or turn it into a pipeline.
You might identify another part of the old loop that also needs to be split.
