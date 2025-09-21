---
layout: refactoring
title: Introduce Parameter Object
source: Martin Fowler
source_url: https://refactoring.com/catalog/introduceParameterObject.html
code_smells: long_parameter_list
learning_hours:
---

# Introduce Parameter Object

This is provided by some tools - Resharper has 'Transform Parameters', IntelliJ has 'Introduce Parameter Object'. If you don't have this available, then this checklist will help you to do it with only Extract Method and Inline Method.

## Identify
In a long parameter list, some might usefully be grouped together into a new class.

## Prepare
Work out which parameters you want to group together into a new class and ideally think of a good name for it.

## Implement

* Before the call site to the method, pretend you already have the new class, declare a variable for it and call its constructor with the arguments you want to put in the new type, eg `var wrapper = ParameterWrapper(a, b, c)`.
* Use your tools to create that class `ParameterWrapper`.
* Store all the constructor arguments in public fields.
* change all the references to these variables to use the fields of your new class, eg `a` becomes `wrapper.a`  
* 'Extract method' on all the code that uses `wrapper`. The method should have the signature you wanted, and call the original method.
* Inline the call to the original method.

## Clear
Check the name of the new method is the same as the original.

## Follow up
Often you want to move the method to the type you just created.
