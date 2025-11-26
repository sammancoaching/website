---
layout: refactoring
title: Replace Function with Command - Static to Instance
source: Martin Fowler
source_url: https://refactoring.com/catalog/replaceFunctionWithCommand.html
code_smells: feature_envy
learning_hours: change_signature
---

# Replace Function with Command - Static to Instance

This is one of the refactorings in Martin Fowler's book. The basic idea is to change a freestanding function into a method on a class. In languages like Java and C# you'd probably call it 'static to instance'. This is the inverse of [Replace Command with Function]({% link _refactorings/command_to_function.md %})

## Examine
Usually the prompt for this refactoring is a need for more flexibility - a method can be overridden in a subclass, it can remember state between invocations, and you can combine it with other methods to make a better overall abstraction. Freestanding functions can have a 'feature envy' code smell with respect to a parameter, and might make more sense to become a method on that parameter's class.

## Prepare
Identify the function you want to turn into a command - that is, a method on an object. Identify whether the class it should be moved to exists already and if not, create it.

## Implement

* Move the function to the class where you want it to become a method.
* Inside the function, introduce a new local variable which is an instance of that class.
* Replace use of function parameters with data members of the class. You may need to add new data members for some or all parameters.
* Introduce Parameter for the instance of the class. Note: if your tool doesn't have this refactoring, see the alternative below.
* Tests all passing.
* Convert the function to a method. This should be straightforward since it has an instance argument that can become 'this' or 'self'.
* Inline all calls to the original function.
* Tests all passing.

## Alternative to Introduce Parameter

Some refactoring tools don't offer this, but you can achieve the same result as long as you have 'extract method' and 'inline method', which are more widely supported.

* Extract method on all the body of the method, excluding the first line which constructs the instance. This new method should have the signature you want - with the instance as an argument
* Inline the original method. This will replace all the places the old method was called with a call to the new method that has the signature you want.

## Clear
Check if there are any unnecessary arguments or variables that should be inlined.

## Follow up
Check whether the method can take advantage of OO design structures, like polymorphism.

