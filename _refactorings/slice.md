---
layout: refactoring
title: Slice
source: Emily Bache
code_smells: long_function
learning_hours: slice
---

# Slice
Emily Bache first learned this refactoring from Llewellyn Falco. This description was written in collaboration with [Willem van den Ende]({% link society/contributors/mostalive.md %})

## Examine
Look for a long function that you want to get under test, where there is a statement somewhere in the middle that makes it hard to test. Usually it refers to a dependency you don't want to include in your unit test. This becomes a candidate for 'slice' if you cannot easily slide this function to the start or the end of the function in order to use [Peel]({% link _refactorings/peel.md %}).

## Prepare
Isolate the smallest possible part that you want to be able to slice out of this function. This will be the part that will be replaced by a mock in a test, so you want to make it as little logic as possible. You might want to extract a variable for the part you will slice so it's separated from the surrounding code.

## Implement

* Replace the code you want to slice with a lambda that does that thing. Invoke it straight away in the same place as before.
* Use 'slide statement' on the definition of the lambda to move it to the top of the method. Leave the invocation in place.
* [Extract Function]({% link _refactorings/extract_function.md %}) on the part below the lambda definition. You now have a new (testable) function that takes the lambda as a parameter.

## Clear
The new code may look more complex because of the lambda parameter. Improve the names of the parameter and any variables that use it to make the code as readable as possible. 

## Follow up
* Move and/or create tests, replacing the lambda with a stub instead of a concrete invocation of the unwanted dependency.
* Move the method to another class where the unwanted dependency is not present
* Check that "everything that could possibly break" is tested - the extracted lambda allows more combinations to be easily tested.
* Replace the lambda with an interface that has only one method.

