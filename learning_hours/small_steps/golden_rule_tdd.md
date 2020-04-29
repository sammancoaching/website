---
layout: default
title: Golden Rule of TDD
parent: Working in Small Steps
grand_parent: Learning Hours
nav_order: 3
---


# Golden Rule of TDD

When people start with TDD I often see them struggle to remember to write the test code first. They may have that intention, but then forget all to easily. This session helps them practice this skill.

## Session Outline
 
* 10 min connect: How to create a class   
* 10 min concept: Golden Rule
* 30 min do: shopping basket
* 5 min reflect: tips to remember the golden rule

### Connect
In your IDE, what different ways are there to create a new class? I mean, ways where you don't have to type anything except the class name and the tool puts in all the relevant language syntax, brackets, package declarations, constructor, superclass etc.

Find as many ways as you can. Search the help and the menus. 

Ask people to come forward and present their discoveries.

Hopefully people will discover lots of useful options. If they don't spot it for themselves, point out that it also works to just start using the class in some other code then auto-complete it into existence. That's the way you can do it from a test.

### Concept: Golden Rule
In TDD the _tests_ drive the design of the production code. You can express that as a golden rule:

**Do not write any production code until you have a failing test that requires it**

Only declare new classes, methods etc, in test code. Then use your tools to bring those things into existence.

Write the golden rule on a flipchart and make it look pretty.

### Do: Shopping Basket
Practice writing the tests first before creating the classes and functions they describe. The [Shopping Basket Kata](../../exercises/kata_descriptions/shopping_basket.html) might be a good one.

### Reflect: How to remember
- How will you remember the golden rule when you are designing new code?
- For example, could you configure your IDE with a new class template containing a comment 'Do you have a test for this?'
- Note some ideas on a post-it to take with you
