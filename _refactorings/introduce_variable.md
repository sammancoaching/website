---
layout: refactoring
title: Introduce Variable
source: Martin Fowler
source_url: https://refactoring.com/catalog/extractVariable.html
code_smells: duplicated_code
learning_hours: law_of_demeter
---

# Extract Variable / Introduce Variable

## Examine
Identify an expression that you'd like to extract as a named variable.

## Prepare
Select the expression. Preferably use the IDE's 'expand selection' functionality to make sure it's a valid expression. Inspect the highlighted code to ensure there are no side effects.

## Implement
IDE: while you have the expression selected, use 'introduce variable' or similar from the refactoring menu.

By hand:
* Copy the selected expression
* Declare a new variable with a suitable name, before the first place the expression is used. Set the new variable to the selected expression using Paste.
* Replace the original expression with the new variable.
* Test.

If the same expression appears in several places, replace the others too, testing after every replacement.

## Clear
Ensure the name of the new variable makes sense in all contexts, Rename if needed.

## Follow up

* You could introduce the variable as a parameter to the enclosing method.
* You could introduce the variable as a field of the enclosing class
* You could slide statement in order to initialize the variable earlier in the code.
* You could extract method on the following section of code that uses the variable, so it will be passed as a parameter to the new method.
