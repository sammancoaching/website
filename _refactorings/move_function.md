---
layout: refactoring
title: Move Function / Move Method
source: Martin Fowler
source_url: https://refactoring.com/catalog/moveFunction.html
code_smells: feature_envy
learning_hours: primitive_obsession
---

# Move Function / Move Method

## Examine
Identify a function or method that you would like to move to a different module, class or namespace.

## Prepare
* Go through the body of the function and consider all the program elements it uses. Should any of them move too? Also consider if the method is polymorphic what should happen to subclasses and superclasses.
* Work out the best order to move things in and make a plan.

## Implement
* IDE: with the cursor on the function declaration, Refactoring menu, Move...

If that doesn't work, these are some manual steps:
* Declare the function in the new module, class or namespace with the signature you want it to have.
* Call the original function from the new place, then [Inline function](inline_function.html) to get the function body into the new place.
  * Note you might need to adjust the old function to make it possible to call it from here.
  * Note if it's not possible to call it from here, you could just copy and paste the function body to the new place and then fix it up to make it work.
* Compile. The new function is there but not used.
* Update the original function to call the new one.
* Test.

At this point you have succeeded in you original aim - the function body is moved to a new place. However, clients of the original method will still be calling that one. 

## Clear
* Now the function is moved, check the access level. It may be able to be private or protected in its new home.

## Follow up
* Use [Inline function](inline_function.html) on the original function. This should update all clients to use the method in its new home and let you remove the original function.
