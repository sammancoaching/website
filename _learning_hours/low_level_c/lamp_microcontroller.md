---
theme: low_level_c
title: TDD a lamp microcontroller
kata: lift_button
difficulty: 3
author: objarni
---

# TDD a lamp microcontroller

This learning hour follows on from the one about TDD in a finite state machine. This time we work on the same problem but instead of working on states and transitions, we focus on the lamp microcontroller logic.

## Learning Objectives

* Recognize that you can use TDD to develop a microcontroller
* use TDD to develop control logic using fake hardware
* discuss the benefits and pitfalls of using fake hardware

## Session Outline
 
* 10 min connect: bit operations  
* 10 min concept: using the fake hardware
* 30 min do: Lift Button
* 5 min reflect: Challenges for test design

### Connect - bit operations

Given this list of bit operations

* `i |= 0x04`
* `i = 0b11111111;`
* `i &= ~ (1 << 2);`
* `i = 0x00`


And these desired outcomes

* Clear bit 2
* Clear all 8 bits
* Set all bits
* Set bit 2

Match them together

You could put these on sticky notes on a whiteboard for example. The idea is to remind people that they know how to do bit manipulation, which will be useful in this exercise.


### Concept - using the fake hardware

We continue to work on a finite state machine simulating a Lift Button but this time the focus is on turning the lamp on and off. In the production code this will be achieved using some bit operations on a port. In the test we need to use a different port memory address, one that we control. This is a kind of fake.

Use the starting code for a [Lift Button](https://github.com/objarni/FiniteStateMachineTDDKata) on the branch 'starting_point_applied_tdd_2'. Demonstrate how to set up the fake port and write the first (failing) test for switching the lamp on.

### Concrete - using TDD with the fake address

Split up and work in pairs implementing the lamp functionality.

### Conclusions - using fake hardware

Ask people if they experienced any challenges or difficulties using the faked hardware. Also if they had any trouble with TDD. Ask people to think about whether TDD is a good approach for embedded development.