---
layout: refactoring
title: Split Variable
source: Emily Bache
source_url: https://refactoring.com/catalog/splitVariable.html
code_smells: variable_with_long_scope
learning_hours: split_variable
---

# Split Variable
This is one of the refactorings in Martin Fowler's book although I think his definition is unnecessarily narrow and I usually extend it to additional situations.

There is a video and other materials available for this learning hour as part of a [Technical Coaching Programme]({% link training/full_package.md %})

## Examine
There are three common situations to use split variable:

1. The same variable is re-used for different purposes. This is the first form of split variable, and the one that Martin Fowler discusses in his book.
2. An accumulating variable where you want to split off part of the calculation to another scope.
3. A global or class data member that is used in many places but only calculated in one place, and you want to split the calculation to a different (smaller) scope.

## Prepare
Identify the variable you want to split, and make sure your tests are all passing.

## Implement
Steps for each of the three situations:

1. Same variable is re-used for different purposes
   * Tests all passing.
   * Identify a variable that needs to be split, 'x'.
   * Within the lines of code you select for the first thing it does, use textual search and replace - rename 'x' to something better.
   * After those lines, re-declare 'x' as a new variable.
   * Tests all passing.

2. An accumulating variable
  * Tests all passing
  * Identify a variable that needs to be split, 'x'
  * Create a new local variable 'increment_x' and initialize it to an empty value eg zero
  * Within the lines of code you select use textual search and replace - rename 'x' to 'increment_x'
  * After those lines, re-assign x += increment_x
  * Tests all passing

3. A global or class variable
  * Tests all passing
  * Identify a variable that needs to be split, 'x'
  * Create a new variable 'x_local' - copy the declaration of 'x' and copy the same initial value as 'x'
  * Within the lines of code you select for the new scope, use textual search and replace to replace x with x_local
  * After that section of code, re-assign 'x' to the value of 'x_local'
  * Tests all passing

## Clear
It usually makes sense to review the names of the new variables and adjust them now you can see how each is used.

## Follow up
Often you now want to extract a method to calculate one or more of the new variables.
