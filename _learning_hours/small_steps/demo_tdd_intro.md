---
theme: small_steps
title: Using TDD to write a Leap Years function
kata: leap_years
difficulty: 1
---

# Using TDD to write a Leap Years function

This is often the first exercise I do with new teams. You have to TDD a function that takes an integer argument and returns a boolean. It ends up being a rather small piece of code, just enough to show a few TDD cycles.

The first time I demonstrate this kata I usually don't show triangulation, and only do the four test cases listed in the problem description. That means I go straight to using the modulo operator when implementing the first test case. That keeps the demo shorter, and means you don't need to explain triangulation as a concept.

## Learning Goals
* Describe the Red-Green-Refactor cycle
* Explain why you write the tests first and not all at once
* Design a pure function that takes an integer and returns a boolean, using TDD

## Session Outline

* 10 min connect: divide into pairs, 3 benefits of TDD  
* 15 min concept: demo leap years  
* 20 min do: leap years in pairs  
* 10 min reflect: summary of main idea 

### Connect
Have everyone stand up and stand at one side of the room. Ask them to walk a few steps towards the other side of the room in proportion to their answers to these questions. More confidence means they should walk further:

- confidence pair programming
- confidence with unit testing
- confidence with Test-Driven Development

Have people form pairs with someone standing in a different part of the room so you get pairs with varying experience. Hopefully these will be good pairs to work in later on in the session.

In your pairs:

- Think of 3 benefits of Test-Driven Development.

After a few minutes of discussion, ask a few pairs to report some of the benefits they thought of to the whole group.

### Demonstrate
Starting at a whiteboard, explain the purpose of the [LeapYear](/kata_descriptions/leap_year.html) kata. Read the description to the group, and/or display it on a slide. Write up all 4 examples given in the kata description on a whiteboard. Note that these will turn into tests.

Demonstrate how to TDD this function, taking one example/test at a time. I often do the demo using cyber-dojo as a development environment, since it makes the TDD cycles visible.


### Do
Have the group work in pairs or a mob to do the Kata again, starting from no code, just the examples written on the whiteboard. Every 4 minutes, remind them to swap the driver. They should do it the same way you demonstrated, test by test in small steps.

Go around the pairs helping them. Remind them to write the tests before the implmentation, working incrementally and iteratively.

### Reflect
- Think about what we did today. If you had to explain the main idea of TDD to someone else, what would you say?
- Write your explanation in a sentence or two on a post-it

Put up a flipchart with the question "What is the main idea of TDD?" and make it look attractive with a lightbulb doodle or something. Ask people to stick their post-it notes on it. Read some notes out to the group. Hang the poster somewhere prominent afterwards, perhaps in the team area or coffee room.
