---
layout: refactoring
title: Inline Function
source: Martin Fowler
source_url: https://refactoring.com/catalog/inlineFunction.html
code_smells: lazy_element
learning_hours: keyboarding
---

# Inline function / Inline method

* Identify a function or method which you would like to replace with its body in some or all of the places it's used. 

## Refactoring steps
* IDE: right click on the function declaration, Refactoring menu | Inline

If that doesn't work, these are some manual steps:
* Find all the callers of the function:
  * IDE: right click on the function declaration, Find Usages.
  * Alternatively - "lean on the compiler" - rename it and see what breaks.
* For each usage: 
  * Comment out the call so you still have it there to refer to. 
  * Copy the function body and paste it into the caller code under where you commented it out. 
  * Fix it up until it compiles.
  * Test.
  * Delete any commented-out code
* Remove the original function definition if and when it is no longer used.