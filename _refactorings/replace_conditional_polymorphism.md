---
layout: refactoring
title: Replace Conditional with Polymorphism
source: Martin Fowler
source_url: https://refactoring.com/catalog/replaceConditionalWithPolymorphism.html
code_smells: repeated_switches
learning_hours: replace_conditional_with_polymorphism
---

# Replace Conditional with Polymorphism

This refactoring replaces conditional logic with classes and polymorphism. The code smell that leads you to it is having a lot of similar switch statements that switch on type.

## Examine
Identify all the places with a repeated switch statement, that switch on the same type and have similar cases. 

## Prepare
All these switches should be in functions on the same class - the one which "has" the type that is being switched on. Extract methods as needed and move them to the class which will become the base of the polymorphic hierarchy.

If the constructor to the class is called in a lot of places it's probably worth first doing 'replace constructor with factory method'.

## Implement

* Create new subclasses for each branch of the conditional. They should be empty with only a call to the superclass constructor
* Replace calls to the constructor of the base type with calls to the relevant subclass constructor. This will probably mean creating a new switch statement.
* 'Push Down' the first method containing the switch/conditional
* Remove redundant code in the pushed down method.
* 'Push Down' any additional fields or methods
* Remove redundant code and make the superclass abstract

## Clear
Consider whether the superclass should be an interface or an abstract class.


