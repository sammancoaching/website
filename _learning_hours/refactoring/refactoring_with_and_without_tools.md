---
theme: refactoring
title: Refactoring with and without tools
kata: tennis
difficulty: 1
author: reasun
tags:  refactoring c
---

# Refactoring with and without tools aka Golden Rule of Refactoring

Do you know what tools you have available? You don't always have the ones you'd like to have, and they don't always work totally reliably. How do you handle that?

## Prerequisite

[Identify Paragraphs]({% link _learning_hours/refactoring/identify_paragraphs.md %})

## Learning Goals

* Get to know the IDE's refactoring tools
* Know and apply the rule to be no more than 1-3 steps away from working code
* Learn how to refactor even when tools are not available or not working

## Session Outline

* 5 min connect: What refactoring tools are you using?
* 20 min concept: Tools, Small Steps, Demo
* 30 min concrete: pairs refactor a suitable kata
* 5 min conclusion: Composing refactorings of small steps?

### Connect

Ask the group - What refactoring tools are you using? Collect comments from the whole group and put them into a shared document or whiteboard. Hopefully they know some of the tools available to them.

This is a [Open Question]({% link _activities/connect/open_question.md %}) connect.

### Concept - Tools

Next ask them to find out which tools their IDE supports, or what plugins are available. Let them write down the results in a shared document or whiteboard. Examples for plugins are: abracadabra for VSCode, resharper for VS.

This is a [Web Hunt]({% link _activities/connect/webhunt.md %}) connect.

Hopefully people will realise that their IDE is much more powerful than they thought.

#### Homework (if this LH is one of a series)

Ask each member of the group to pick a tool they don't use often enough (or haven't used before) and to make an effort to use it more often in the coming week(s). You will ask them about it in the next session.

### Concept - Refactoring steps

Ask the group - Why would you want to refactor without tools?

Introduce them to the Golden Rule: Never be more than 1-3 steps away from working code. This means that you can undo your changes back to a working state in one to three steps, but also that you will reach a new, working state in one to three steps. This sequence of small transformations produces a significant restructuring. At the same time, each transformation is so small, it is less likely to go wrong.

Reference Martin Fowler's Refactoring book to bring across the notion of proven step-by-step recipes for refactorings. (For all languages and IDEs, regardless of the tools available)

We don't always have all tools for all languages available, and some refactorings are sequences of smaller refactorings. -> Golden Rule applies

### Demo

Demo an example refactoring using small steps, e.g. the steps to Extract Method. Other options of similar complexity (depending on prior knowledge of the group) include Move Function, and Introduce Parameter Object.

1. Copy the block of code into the clipboard (copy, not cut).
1. Create a new, empty void method with no arguments. Give it a nonsensical name like 'foo' or 'applesauce'.
1. Paste the code from the clipboard into that method.
1. Figure out what the return type should be and change the method to return it.
1. Figure out what the arguments should be and change the method to use them.
1. After having worked with the code, you should have an idea what the code does. Rename the method to reflect this.
1. Compile and test.
1. Replace the original paragraph with a call to the method.
1. Compile and test.

### Concrete

Work on a refactoring exercise that needs the refactoring you have demoed, for example [Tennis]({% link _kata_descriptions/tennis.md %}). Have people use the steps you showed them earlier.

Choose an exercise that already has good, fast tests.

### Conclusions

Ask people to think about how they would have used various refactoring tools for the whole refactoring or individual steps. Which refactoring could we compose out of these small steps?

This is a variant of [When To Use This]({% link _activities/conclusions/when_to_use_this.md %}).
