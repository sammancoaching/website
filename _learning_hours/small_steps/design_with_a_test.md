---
theme: small_steps
title: Design in the Red step
name: design_in_red_step
kata: lift_button
difficulty: 1
author: emilybache
---

# Design in the Red step

When you've got an IDE it's very convenient to create classes and method directly from the test case.

## Learning Objectives

* Remember to design new classes and functions in the test, before they exist
* Use the capabilities of the IDE to create classes and functions from the test 

## Session Outline

* 5 min connect: How to create a class
* 10 min concept: Design in TDD - in the red step
* 30 min do: Lift Button
* 5 min reflect: note down the keyboard shortcuts

### Connect - ways to create a class

Put up the IDE on the big screen, with an empty project and empty test case open. Ask "I'd like to create a new class, called LiftButton. What should I do? Please navigate me". Hopefully someone will ask you to use the new class wizard or similar. Create the class as they instruct. Ask again - is there any other way to create a class? Hopefully someone eventually will tell you to write `new LiftButton()` (or similar) in the test case. Bingo. Make sure they see how you use the tool to summon the new class into existence from the test.

(Of course if no-one suggests this you show them anyway)

### Concept: Design in TDD - the red step
The test is the first time you use the class or method. Before you use the tool to summon it into existance, you can examine how easy it is to use your design. It's the cheapest possible moment to change your design decisions.

### Do: Lift Button
Practice writing the tests first before creating the classes and functions they describe. The [Lift Button Kata]({% link _kata_descriptions/lift_button.md %}) might be a good one.

Before you split into pairs to work on the kata, spend a few minutes in the whole group coming up with a test list. Something like:

- button not pressed, doors closed, light off
- button is pressed, doors closed, light on
- button is pressed, doors open, light off
- button not pressed, doors open, light off

When they are doing the kata, try to stop them from creating any functionality without first creating a test case. Have them practice using things in the test _before_ they exist in the production code.

### Reflect: keyboard shortcuts
Which keyboard shortcuts did we use to create things? Make a note so you remember them. 

