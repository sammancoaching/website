---
theme: testable_design
title: Bottom-up design
kata: yatzy
difficulty: 2
author: emilybache
tags: testable_design
---

# One function at a time, bottom up

This kata is a couple of steps up in difficulty from Leap Years. You are designing one main function with several helper functions. You test drive the implementation one helper function at a time. The group learns about this strategy for breaking down a problem into pieces suitable for TDD.

## Learning Goals
The theme continues on designing testable code.

* Solve a problem by breaking it into independently testable pieces
* Distinguish between overdesign and testability

## Session Outline

* 5 min Connect: "Take a Guess" with topic Overdesign   
* 10 min explain yatzy & make list of test cases together  
* 10 min mob with you navigating  
* 30 min mob continues 
* 5 min Reflect: whole group temperature - too many/too few tests?  

## Connect
The topic is _overdesign_ in software. Read the list of statements below. Circle those that are relevant to the topic, and cross out those that are unrelated. Compare your answers with your neighbour.

* All problems in computer science can be solved by another level of indirection ...except for the problem of too many layers of indirection.
* Boundary condition analysis is useful in test design.
* Abstract Factory is a design pattern.
* "You Aint Gonna Need It" is a poor excuse used by failed designers to justify deleting useful extension points in the software design.
* In code reviews, you should suggest replacing any global variables with the Singleton pattern.
* Primitive Obsession is a code smell.
* UML is a graphical language for describing software design.
* Premature Generalization is a code smell.
 
## Demonstrate
Starting at a whiteboard, explain the purpose of the [Yatzy]({% link _kata_descriptions/yatzy.md %}) kata. Read the description to the group, and put the category and scoring rules on a screen they can see. Ask the group if they can see any examples in the description that would make good test cases. There are lots! For example they might find these examples:

* 1,1,3,3,6 placed on “chance” scores 14 (1+1+3+3+6)
* 1,1,1,1,1 placed on “yatzy” scores 50

When they've identified these, ask the group what order they would tackle the examples in. When some consensus arises, note this on the whiteboard. I expect they would want to order by category, for example:

- Small straight: 1,2,3,4,5 scores 15
- Large straight: 2,3,4,5,6 scores 20
- Chance: 1,1,3,3,6 scores 14
- Yatzy: 1,1,1,1,1 scores 50
- Yatzy: 1,2,3,4,5 scores 0
- ...

Don't worry too much about what order they want to do the categories in, although I do suggest you encourage them to tackle ones, twos etc before tackling pair or full house.

Take the navigator role in the mob, rotate the driver. Steer the group towards a design where you have a function for each yatzy category, and some kind of switch statement in the main function that calls them. Each such function is named after the category, takes a list of five integers, returns an integer. You should get at least as far as creating the first of those functions.

## Do
Hand over the navigator role to someone in the mob, continuing to code from where you got to. Make sure they continue to work in small steps, implementing function by function and keeping all the tests passing.

## Reflect
In pairs, discuss:
- How did we break down the problem into pieces for TDD?
- Is each piece of the design testable by itself?
- Do we suffer from overdesign?
