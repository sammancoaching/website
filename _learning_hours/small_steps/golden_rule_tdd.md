---
layout: learning_hour
title: Golden Rule of TDD
parent: Working in Small Steps
grand_parent: Learning Hours
nav_order: 3
---


# Golden Rule of TDD

When people start with TDD I often see them struggle to remember to write the test code first. They may have that intention, but then forget all to easily. This session helps them practice this skill.

## Session Outline
 
* 10 min connect: How to create a class / TDD things to remember  
* 10 min concept: Golden Rule
* 30 min do: shopping basket
* 5 min reflect: tips to remember the golden rule

### Connect - ways to create a class
(use this connect if you are using an IDE that can create classes and methods)

In your IDE, what different ways are there to create a new class? I mean, ways where you don't have to type anything except the class name and the tool puts in all the relevant language syntax, brackets, package declarations, constructor, superclass etc.

Find as many ways as you can. Search the help and the menus. 

Ask people to come forward and present their discoveries.

Hopefully people will discover lots of useful options. If they don't spot it for themselves, point out that it also works to just start using the class in some other code then auto-complete it into existence. That's the way you can do it from a test.

### Connect - things to remember when doing TDD
Instead of the above connect, do this learning hour a second time as a refresher, with a different connect.

Put this question to the group, and ask them to come up with 5 answers.

"What are 5 important things to remember when you're doing Test-Driven Development?"

The kinds of answers you're looking for are:

- take small steps, testing one thing at a time
- run tests often
- refactor test code as well as production code
- only refactor when tests are passing
- make a test list
- write the test first

The 'concept' part of this learning hour emphasizes the 'write the test first' guideline, but you can also write up and highlight the other guidelines they come up with.

### Concept: Golden Rule
In TDD the _tests_ drive the development of the production code. You can express that as a golden rule:

**Do not write any production code until you have a failing test that requires it**

Declare new classes, methods etc, in test code. Then use your tools to bring those things into existence.

Write the golden rule on a flipchart and make it look pretty. Ask people what they think of it.

You might mention there is an exception to the Golden Rule: you are allowed to declare new classes and methods while refactoring, so long as they are already covered by existing tests.

### Do: Shopping Basket
Practice writing the tests first before creating the classes and functions they describe. The [Shopping Basket Kata](../../exercises/kata_descriptions/shopping_basket.html) might be a good one.

### Reflect: Will you try using this rule?
What do you think about this rule? Will you try to use it?

- Discuss in pairs or small groups
- Note a reminder of the rule on a post-it to take with you

Homework: note down situations when you do and don't use the rule until the next learning hour

