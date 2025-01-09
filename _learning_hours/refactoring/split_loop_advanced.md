---
theme: refactoring
title: Split Loop (Advanced)
name: split_loop_advanced
code_smell: divergent_change
kata: theatrical_players
difficulty: 3
author: emilybache
---


# Split Loop (more difficult version)

Divergent Change is a code smell that describes when the same section of code needs to change because of several different reasons. It would be better to divide up the responsibilities. This learning hour is similar to the one on [Split Loop]({% link _learning_hours/refactoring/split_loop.md %}) but is intended to show the more advanced version of the split loop refactoring.

# Learning Goals

* Use "Split Loop" to separate concerns into different parts of the code when there are awkward local variables

# Session Outline
* 10 min connect: Classify the code
* 10 min concept: Make the Change Easy
* 5 min demo: Split Loop (advanced)
* 35 min do: Split loop in Theatrical Players and Office Cleaning Robot
* 5 min reflect: Explain the main idea


## Connect: Classify the code
Give people copies of the code for [Office Cleaning Robot](https://github.com/sammancoaching/OfficeCleaningRobot-Refactoring-Kata) version 1 in a format they can sketch on, like paper or an online activity board. Give them three colours of pen to mark sections of code that have these concerns:

* Parsing input commands
* Moving the Robot Cleaner
* Unclear or mixed

Also ask them to think about what design principles this code might break, or if there are any obvious code smells.

When everyone has had a chance to read the code and colour it, gather together and talk about what you found. The code should be stripy - mixed concerns all over the place. People might talk about problems with the Single Responsibility Principle or with Divergent Change. If they don't mention these things, don't worry, you'll explain in the next part.

## Concept: Divergent Change
Explain that the reason you wanted them to classify the code like this is because the next features that will be developed are

* Input commands in JSON format
* Display the track of the robot's movement

Looking at the top level loop in 'parseInput', this code suffers from [Divergent Change]({% link _code_smells/divergent_change.md %}). This loop does two things that don't need to be together. We'd like to refactor the code before we begin developing new features. As Kent Beck says 'make the change easy (warning: this may be hard), then make the easy change'.

## Demo: Split loop
In either [Theatrical Players](https://github.com/emilybache/Theatrical-Players-Refactoring-Kata) or [Office Cleaning Robot](https://github.com/sammancoaching/OfficeCleaningRobot-Refactoring-Kata) (version 1) show that you need to do several refactorings in order to separate the different kinds of logic. Show how to do that safely, including [Split Loop]({% link _refactorings/split_loop.md %}). Use the more advanced form where you create a new class to hold the local variables.

## Concrete Practice: Split loop in Theatrical Players and Office Cleaning Robot
In pairs, do the same split loop in both [Office Cleaning Robot](https://github.com/sammancoaching/OfficeCleaningRobot-Refactoring-Kata) (version 1) and Theatrical Players.

## Conclusions: Explain the main idea
[Explain the main idea]({% link _activities/conclusions/explain_main_idea.md %}) If someone asked you when and how to do 'split loop', what would you tell them? Everyone note down their ideas individually.


