---
theme: low_level_c
title: TDD a state machine
kata: lift_button
difficulty: 2
author: objarni
affiliation: ProAgile
tags: c small_steps
---

# TDD a state machine

A state machine is a very specific way to organize the logic in your application. In this learning hour we practice building the state machine iteratively and incrementally with TDD.

## Learning Objectives

* Recognize that you can use TDD to develop a state machine
* use TDD to develop a state machine with two signals and two states
* discuss whether TDD is a reasonable approach to developing state machines generally

## Session Outline
 
* 10 min connect: What test cases would you write?  
* 10 min concept: One state at a time
* 30 min do: Lift Button
* 5 min reflect: would this approach work for larger state machines?

### Connect - tests for a state machine

We're assuming the participants already know about making a test list - so we ask them to make a test list for a state machine with two states and two transitions:

![Lift Button State Diagram](/assets/images/lift_button_states_transitions.png)

### Concept - how to TDD a state machine

There is some starting code for a [Lift Button](https://github.com/objarni/FiniteStateMachineTDDKata). On the branch 'starting_point_applied_tdd_1' you will find a partial implementation of a state machine, together with a half-finished test list. The idea is to get the participants going more quickly developing a finite state machine by having them continue from this point.

In this part of the learning hour we need to go through the code, explain what's already been done, or perhaps better, demo getting to this point.

### Concrete

Let the participants take over the code from this point and continue to develop the finite state machine.

### Conclusions

Discuss what it was like developing a FSM using TDD. Would this approach scale to larger and more complex state machines?
