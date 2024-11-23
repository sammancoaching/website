---
theme: small_steps
title: Using TDD to write a Leap Years function
kata: leap_years
difficulty: 1
author: emilybache
---

# Using TDD to write a Leap Years function

This is often the first exercise I do with new teams. You have to TDD a function that takes an integer argument and returns a boolean. It ends up being a rather small piece of code, just enough to show a few TDD cycles.

The first time I demonstrate this kata I usually don't show triangulation, and only do the four test cases listed in the problem description. That means I go straight to using the modulo operator when implementing the first test case. That keeps the demo shorter, and means you don't need to explain triangulation as a concept.

There is a video on Emily Bache's YouTube channel for this learning hour - ["TDD - What it is and why you should care"](https://youtu.be/OhT0_Xg-vZU)

## Learning Goals
* Describe the Red-Green-Refactor cycle
* Design a pure function that takes an integer and returns a boolean, using TDD

## Session Outline

* 10 min connect: divide into pairs, 3 benefits of TDD  
* 15 min concept: demo leap years  
* 20 min do: leap years in pairs  
* 10 min reflect: summary of main idea 

### Connect
In pairs:

- Think of 3 benefits of Test-Driven Development.

After a few minutes of discussion, ask a few pairs to report some of the benefits they thought of to the whole group. Write up what they say on a whiteboard or shared document.

Note - if you don't think the group knows enough about TDD to be able to come up with any benefits of it, ask about the benefits of unit testing in general.

### Demonstrate
Starting at a whiteboard, explain the [LeapYear](/kata_descriptions/leap_years.html) kata. Read the description to the group, and/or display it on a slide. Write up all 4 examples given in the kata description on a whiteboard. Note that these will turn into tests.

Demonstrate how to TDD this function, taking one example/test at a time. I often do the demo using cyber-dojo as a development environment, since it makes the TDD cycles visible.

### Do
If you're using cyber-dojo for the exercise, spend a few minutes explaining how to use it. Make sure they know how to switch typist if they are working remotely. (Outgoing typist runs the tests, incoming typist refreshes the page).

Have the group work in pairs or a mob to do the Kata again, starting from no code, just the examples written on the whiteboard. Every 4 minutes, remind them to swap the typist. (Or give them an online ensemble timer). They should do it the same way you demonstrated, test by test in small steps.

Go around the pairs helping them. Remind them to write the tests before the implementation, working incrementally and iteratively.

If any of the pairs are really quick and don't need as long as 20 minutes, they could additionally do TDD on another exercise - for example [Closest to zero](/kata_descriptions/closest_to_zero.html). Encourage them to make a test list before they begin coding.

### Reflect
- Think about what we did today. If you had to explain the main idea of TDD to someone else, what would you say?
- Write your explanation in a sentence or two on a post-it or shared document

#### Visual reminder
Put up a flipchart with the question "What is the main idea of TDD?" and make it look attractive with a lightbulb doodle or something. Ask people to stick their post-it notes on it. Read some notes out to the group. Hang the poster somewhere prominent afterwards, perhaps in the team area or coffee room.

If you're working remotely, then set this homework: ask people to give their explaination of TDD to another colleague who wasn't in the session and note down their reaction.
