---
layout: refactoring
title: Inline Function / Inline Method
source: Martin Fowler
source_url: https://refactoring.com/catalog/inlineFunction.html
code_smells: lazy_element
learning_hours: keyboarding
---

# Inline Function / Inline Method

## Examine
Identify a function or method which you would like to replace with its body in some or all of the places it's used. 

## Prepare
If you plan to remove the original function or method, you should make a list of all the places it is used so you can go through and inline them one by one. If you only want to inline some usages, then you probably don't need to.

* IDE: with the cursor on the function declaration, Find Usages.
* Alternatively - "lean on the compiler" - rename it and see what breaks.

## Implement
* IDE: with the cursor on the function declaration, Refactoring menu, Inline

If that doesn't work, these are some manual steps:
* For each usage you want to inline: 
  * Comment out the call so you still have it there to refer to. 
  * Copy the function body and paste it into the caller code under where you commented it out. 
  * Fix it up until it compiles.
  * Test.

## Clear
* Delete any commented-out code
* Remove the original function definition if and when it is no longer used.

## Follow up
If you have inlined something in a lot of places you may have created duplication. You may want to extract a new method for some or all of it.