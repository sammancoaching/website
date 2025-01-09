---
layout: refactoring
title: Split Loop
source: Emily Bache
source_url: https://refactoring.com/catalog/splitLoop.html
code_smells: loops, divergent_change, shotgun_surgery
learning_hours: split_loop, split_loop_advanced
---

# Split Loop
This is one of the refactorings in Martin Fowler's book. Often this refactoring opens up for a lot of other useful changes.

## Examine
A loop is of itself a code smell, but even more so when it does more than one thing, which implies Divergent Change.

## Prepare
Identify the loop you want to split, and in particular which lines within it that hang together and need to be separated from the others. You may need to do some 'introduce variable' refactorings and 'slide statement' refactorings to gather all the relevant parts of the loop together.

You may discover there are local variables that you will eventually need in both halves of the split loop. There are two main ways to deal with these local variables:

* Re-calculate the variable every time you need it.
* Create a new class and collection for the second loop.

The first option is simpler, but in many cases re-calculation may be costly or impossible. The second option avoids re-calculating the variables every time you need them but is more difficult to do. The mechanics of both are outlined below.

## Implement

### Simple version
This version is for when you have already dealt with any local variables that will be needed in both halves of the loop:

* Tests all passing
* Select the whole loop and duplicate it.
* In the second copy of the loop, delete _everything except_ the lines you want to split.
* In the first copy of the loop, delete _only_ the lines you want to split.
* Tests all passing.

### Advanced version
This version is for when you have local variables you will need to use in both halves:

* Tests all passing
* Identify all local variables needed by the part of the loop you want to split out.
* Create a new class 'LocalData' with fields for all these local variables and a constructor that initializes them.
* Create an instance of the new class called 'localData'.
* Tests all passing ('localData' is not yet used).
* Change the rest of the loop to use 'localData' members instead of the local variables directly.
* Tests all passing.
* Create a new collection before the loop to hold all the instances of 'localData', and in the loop, append the 'localData' instances to the collection.
* Tests all passing ('localData' collection is not used).

Now split the loop:

* Select the whole loop and duplicate it.
* In the second copy of the loop, delete everything except the lines you want to split.
* In the first copy of the loop, delete _only_ the lines you want to split.

At this point the code is broken because there are references to 'localData' in the second loop. 

* Change the second loop to instead use your new collection of 'localData' instances instead of what it was looping over before. 
* Tests all passing

## Clear
Double-check the remaining logic in the original loop makes sense and that you didn't delete too much by mistake. Adjust names for loop variables - something better than 'localData'. You may want to split the original loop again to separate calculation of 'localData' from the rest of the logic.

## Follow up
Often you now want to extract a method for the new loop, or turn it into a pipeline.
You might identify another part of the old loop that also needs to be split.
