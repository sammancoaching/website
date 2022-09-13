---
layout: refactoring
title: Move Function
source: Martin Fowler
source_url: https://refactoring.com/catalog/moveFunction.html
code_smells: feature_envy
learning_hours: primitive_obsession
---

# Move Function / Move Method

* Identify a function or method that you would like to move to a different module, class or namespace.
* Go through the body of the function and consider all the program elements it uses. Should any of them move too? Also consider if the method is polymorphic what should happen to subclasses and superclasses.
* Work out the best order to move things in and make a plan.

## Refactoring steps
* IDE: right click on the function declaration, Refactoring menu | move...

If that doesn't work, these are some manual steps:
* Copy and paste the function to the new module, class or namespace
* If it doesn't compile straight away, undo the copy/paste. Adjust the function in the original place before trying again. Adjustments:
  * Add additional parameters to the function for variables that are available in the source position and not the destination.
  * Extract another method from inside the one you want to move, that has the signature you want, and move that instead.
* When you have a function in the new place which compiles, make the source function call it.
* Test.

At this point you have succeeded in you original aim - the function body is moved to a new place. However, clients of the original method will still be calling that one. 

Follow-up refactorings:

* Use [Inline function](inline_function.html) on the original function. This should update all clients to use the method in its new home and let you remove the original function.