---
layout: refactoring
title: Replace Primitive with Object
source: Martin Fowler
source_url: https://refactoring.com/catalog/replacePrimitiveWithObject.html
code_smells: primitive_obsession
learning_hours: primitive_obsession
---

# Replace Primitive with Object

## Identify
Identify a field or variable that has a primitive type, which you would like to replace with an object of a more meaningful class.

## Prepare
Apply [Encapsulate Variable](encapsulate_variable.html) on the field or variable (if it isn't already encapsulated). This will minimize the number of places that will break when you cut over from the primitive type to the new type.

## Refactor
* Create the new class and name it well.
  * IDE: right click on source folder: "New... Class" or "Add Class". 
* Compile / run static checks.
* Declare the primitive field or variable as a field on the new class.
* Compile / run static checks.
* Initialize the value of the field in the constructor.
  * IDE: with the cursor on the field, context menu, "add as parameter to the constructor" or "Generate constructor"
* Compile / run static checks.
* Add getters and setters for the field on the new class.
  * IDE: with the cursor on the class declaration, Generate... "Getters and Setters" or "Properties"
* Change the type of the primitive to the new class. This will break the compilation / static checks. Fix that:
  * Update the setter and/or the constructor to create an instance of the new class. Pass the primitive value to the constructor of the new class.
  * Update the getter to return the result of invoking the getter of the new class.
* Test.

At this point you've succeeded in you original aim - the primitive type is internally stored as an object with a meaningful class instead. You probably have more work to do though.

## Clean
* Remove any unused getters and setters.

## Follow up

* If the new class doesn't have a unique identity, you could make it immutable (make it a Value Object).
* Use [Move Function](move_function.html) to move relevant methods or functions to the new class.
* Consider whether anything in the new or old place needs renaming.
* If you have clients that use the getter and receive a primitive you could update them to use the new class instead.
* If you have clients that use the setter or constructor to pass in a primitive, you could update them to use the new class instead.
