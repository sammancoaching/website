---
layout: refactoring
title: Replace Conditional Logic with Strategy
source: Joshua Kerievsky
source_url: https://www.industriallogic.com/refactoring-to-patterns/catalog/conditionalWithStrategy.html
code_smells: deep_nesting
learning_hours: 
---

# Replace Conditional Logic with Strategy

This is one of the refactorings in Joshua Kerievsky's book. It is usually done as an initial step before the refactoring "Conditional to Polymorphism" in Fowler's book.

## Examine
Usually the prompt for this refactoring is unnecessary conditional complexity with deep nesting. In particular, when the program is changing behaviour based on a type code or a particular fixed set of conditions. If the class currently containing this behaviour is plausibly going to become the superclass in the Strategy pattern, then you could just extract a method and then go directly to "Conditional to Polymorphism."

## Prepare
* Highlight the block of code you intend to replace with the strategy pattern. It should contain all the conditional logic you want to replace. If the logic is contained in a loop, leave that outside.
* Think of a good class name for the strategy class, note it in a comment 'xxxStrategy'

## Implement

* 'Extract function' for the code you identified. 
* If the new function is not static or top-level, there are additional steps:
  * 'Introduce Parameter' for any data members it uses
  * If necessary, introduce a parameter for an instance of the enclosing class so it can access methods on that class.
  * Make the new method static or top-level
* Examine the parameter list to the new function and identify those that are specific to one strategy. [Introduce Parameter Object]({% link _refactorings/introduce_parameter_object.md %} for those parameters, name the new class as you identified earlier - 'xxxStrategy'. If there are no such arguments, just create that class.
* Make sure the new class is declared as a local variable before you call the new function, and is a parameter to it. Use 'Introduce Variable' or 'Change Signature' if needed.
* 'Move' the static or top level function to the new class as a static method or top-level function in the same file.
* For the new function, 'Make non-static' on the new class. If your tool doesn't have that then these are the steps:
  * Manually put the function inside the class or remove the 'static' modifier.
  * One of the arguments will be the xxxStrategy class that you added earlier. Assign this variable to the enclosing instance `var wrapper = this`. Remove the parameter.
  * Inline the `wrapper` variable
  * Update the call sites so `foo(wrapper)` becomes `wrapper.foo()`

## Clear
Check the names of the new method and class make sense. Check all the parameters to the new method make sense. Some of them might want to become constructor arguments or you might want to move additional methods to this class.

## Follow up
Use 'Replace Conditional with Polymorphism' to make the concrete strategy classes.


