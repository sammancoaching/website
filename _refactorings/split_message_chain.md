---
layout: refactoring
title: Split Message Chain
source: Emily Bache
source_url: https://refactoring.com/catalog/replacePrimitiveWithObject.html
code_smells: message_chains
learning_hours: law_of_demeter
---

# Split Message Chain

## Identify
What you're looking for is code that has chained dependencies - it talks to a "friend's friend". A "friend" is a parameter of the current method, an object you constructed, or an attribute of the current class. Identify which object is the "friend" that you are ok to talk to, but that gives you access to other objects that you don't want to depend on directly.

The unwanted dependency could be obvious if you have a clear [Message Chain]({% link _code_smells/message_chains.md %}), like A.getB().getC(). In that example the "friend" is A, and the "friend's friend" is the thing returned by "A.getB()".

## Prepare
If you don't have a variable for the "friend" object, create one using [Introduce variable]({% link _refactorings/introduce_variable.md %}).

## Refactor
* [Extract method]({% link _refactorings/extract_function.md %}) on the section of code containing the dependency. One of the arguments to the new method must be the "friend" - usually the variable you just introduced
* [Move method]({% link _refactorings/move_function.md %}) - to the "friend" class
* Test.

## Clean
* Check if you should inline the variable you introduced in the prepare step.

## Follow up
* Go to the new method in the "friend" class. It may have further message chains that you can treat in the same way.
