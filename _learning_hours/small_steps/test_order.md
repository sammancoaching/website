---
theme: small_steps
title: Test Order
kata: yatzy
difficulty: 1
author: emilybache
affiliation: ProAgile
---

Test Order with Yatzy
------------------------

This kata is a couple of steps up in difficulty from Leap Years. You are designing one main function with several helper functions. You test drive the implementation one helper function at a time. The group learns about this strategy for breaking down a problem into pieces suitable for TDD.

## Session Outline

* 2 min connect: pairs discuss when to write tests or not  
* 10 min explain yatzy & make list of test cases together  
* 10 min mob with you navigating  
* 30 min mob continues 
* 5 min reflect: whole group temperature - too many/too few tests?  

### Connect
- Do you usually write one unit test for every class and method? 
- Note down your personal policies for when you write a test and when you don't.
 
### Demonstrate
Starting at a whiteboard, explain the purpose of the kata. Read the description to the group, and put the category and scoring rules on a screen they can see. Ask the group if they can see any examples in the description that would make good test cases. There are lots! Ask the group what order they would tackle the examples in, note this on the whiteboard. I expect they would want to order by category, for example:

- small straight
- large straight
- chance
- ones
- twos, threes, fours, fives, sixes
- three of a kind
- four of a kind
- yatzy
- ...

Don't worry too much about what order they want to do the categories in, although I do suggest you encourage them to tackle ones, twos etc before tackling pair or full house.

Take the navigator role in the mob, rotate the driver. Steer the group towards a design where you have a function for each yatzy category, and some kind of switch statement in the main function that calls them. Each such function is named after the category, takes a list of five integers, returns an integer. You should get at least as far as creating the first of those functions.

### Do
Hand over the navigator role to someone in the mob, continuing to code from where you got to. Make sure they continue to work in small steps, implementing function by function and keeping all the tests passing.

### Reflect
- How did we break down the problem into pieces for TDD?
- How much test code do we have compared with production code?
- Have we over-tested or under-tested or got it right, in your opinion? Compare notes with the person next to you.
- Take a whole-group temperature about whether there are too many tests, not enough or about right.


