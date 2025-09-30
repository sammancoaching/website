---
layout: refactoring
title: Split Phase
source: Emily Bache
source_url: https://refactoring.com/catalog/splitPhase.html
code_smells: loops, divergent_change, shotgun_surgery
learning_hours: split_phase
---

# Split Phase
This is one of the refactorings in Martin Fowler's book. Often this refactoring opens up for a lot of other useful changes.

## Examine
Look for one section of code that is doing two separate things - ie you have [Divergent Change]({% link _code_smells/divergent_change.md %}).

## Prepare
Identify the two concerns you want to split. You may need to do some 'introduce variable' refactorings and 'slide statement' refactorings to gather all the relevant parts together. Aim for two sections of code that each do one thing. There will probably be a number of variables which are calculated in the first section and used in the second section.

## Implement

* Tests all passing
* Identify the two sections of code that you want to separate. Slide statement as necessary to create whitespace between them.
* Tests all passing
* Imagine a new class 'LocalData' exists. Between the two sections of code, initialize an instance of it. 
* Identify all local variables needed by the second section of code that are calculated in the first section. (One way to do this is use a tool to 'extract method' on the second section - the argument list to the new method contains these.) 
* Pass all these variables to the constructor of 'LocalData'.
* Use tools to create the class 'LocalData'. Create public fields for all the data.
* Tests all passing ('localData' is not yet used).
* Change the second section of code to use 'localData' instead of the local variables.
* Tests all passing.

## Clear
Adjust names for classes and variables - something better than 'LocalData'. 

## Follow up
It often makes sense to Extract methods for the first and second sections - the return type of the first method is LocalData, the argument to the second is LocalData.

If the two sections of code are in the same loop, you should now split it. There is a useful trick for making this easier:

* Create a new collection before the loop to hold all the instances of 'localData', and in the loop, append the 'localData' instances to the collection.
* Tests all passing ('localData' collection is not used).

Now [split the loop]({% link _refactorings/split_loop.md %}):

* Select the whole loop and duplicate it.
* In the second copy of the loop, delete everything except the lines you want to split.
* In the first copy of the loop, delete _only_ the lines you want to split.

At this point the code is broken because there are references to 'localData' in the second loop.

* Change the second loop to instead use your new collection of 'localData' instances instead of what it was looping over before.
* Tests all passing

Often you now want to turn both loops into pipelines, and/or start making LocalData into a proper domain class and moving methods to it.
