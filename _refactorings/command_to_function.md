---
layout: refactoring
title: Replace Command with Function
source: Martin Fowler
source_url: https://refactoring.com/catalog/replaceCommandWithFunction.html
code_smells: lazy_element
learning_hours: change_signature
---

# Replace Command with Function - Instance to Static

This is one of the refactorings in Martin Fowler's book. The basic idea is to change a method that needs an instance of a class with a freestanding function. In languages like Java and C# you'd probably call it 'instance to static'. This is the inverse of [Replace Function with Command]({% link _refactorings/function_to_command.md %})

## Examine
Usually the prompt for this refactoring is unnecessary complexity - a plain function can be simpler than constructing an object and calling a method on it.

## Prepare
Identify the command you want to turn into a function, and find all the places it is used.

## Implement

* For the first place where the command is used, use 'extract function' to create a new function that both constructs the object and calls the command.
* Introduce parameters for all the necessary data used by the new function
* (optional) Move the new function to a place where it can access object internals for the command it is calling (ie to the class of the object it is constructing) 
* For all the other places where the command is used, have them call the new function instead.
* Tests all passing.
* In the new function, inline the call to the command.
* In the new function, inline the call to the constructor and instead use parameters directly.
* Tests all passing.
* Remove any dead code

## Clear
Check again whether the new function is in the right place. 

## Follow up
Check whether the function has feature envy on any of its arguments. Perhaps it should be moved and become a method on that class - in which case you can use the inverse of this refactoring - [Replace Function with Command]({% link _refactorings/function_to_command.md %}).

