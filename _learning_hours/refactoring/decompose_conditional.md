---
theme: refactoring
title: Decompose Conditional
kata: diagram_printer
difficulty: 3
author: emilybache
tags:  refactoring
name: decompose_conditional
---

# Decompose Conditional
This is one of the refactorings from Martin Fowler's book.

## Learning Goals

* Describe the refactoring "Decompose Conditional"
* Use refactoring tools to decompose a conditional

## Session Outline

* 5 min connect: What is clean & tidy code?
* 5 min concept: Decompose Conditional
* 10 mins demo: TennisGame6, using IDE shortcuts
* 25 min do: Diagram Printer in pairs
* 5 min conclusions: Explain the main idea

### Connect - What is clean & tidy code?
[Pick the correct items]({% link _activities/connect/pick_the_correct_items_on_the_list.md %}) from a list like this:

* Write a comment explaining every line of code
* Instead of duplicating code, extract a method
* Leave unused variables in code comments for future reference
* Use short variable names like a,b,c
* ... your own ideas here

The idea is to get them thinking about what makes code good and readable.

### Concept - Decompose Conditional
This is one of the refactorings from Martin Fowler's book, explain what it is and why you might want to do it.

### Demo - TennisGame6
TennisGame6 from [Tennis Refactoring Kata](https://github.com/emilybache/Tennis-Refactoring-Kata) is designed to have a conditional that is easy to decompose. With your refactoring tools you should be able to do it quite quickly and show a version that is much easier to read and understand.

### Exercise - Tennis & DiagramPrinter
Get them first to repeat what you did with TennisGame6. If they are already quite good with their tools then they will also have time to work on [DiagramPrinter](https://github.com/emilybache/DiagramPrinter-Refactoring-Kata.git) - use the 'with_tests' branch. Ask them to work on decomposing and improving conditional logic in DiagramPrinter.doPrint() and DiagramPhysicalPrinter.doPrint().

### Conclusions - explain the main idea
[Explain the main idea]({%  link _activities/conclusions/explain_main_idea.md %}) of 'Decompose Conditional'.
