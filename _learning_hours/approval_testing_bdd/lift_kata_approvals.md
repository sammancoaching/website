---
layout: default
title: Lift Kata with Approvals
parent: Behaviour Driven Development with Approval Testing
grand_parent: Learning Hours
nav_order: 2
---

# Lift Kata with Approvals

Approval testing can be used for getting legacy code under control. That's how we use it in the Gilded Rose Refactoring kata for example. You can also do new development with this approach. You use a form of Double-Loop TDD. You start with a sketch, and use that as the expected value in the outer loop test. This test fails as long as the program output is different from the sketch. When you've done some development work and the sketch matches the actual output, you approve that and the test passes. Then you can start on the next iteration loop with a new sketch of a different scenario.

## Session Outline
 
* 2 min connect: Approval testing kata bingo  
* 5 min concept: Introduce the Lift Kata
* 10 min concept: choose a scenario and sketch 
* 40 min practice: pair on Lift Kata  
* 5 min reflect: compare test cases to sketch

### Connect
Ask people to call out katas they have done using Approval testing. Write them on a whiteboard

Put a mark by those are Refactoring katas. Approval testing is a popular technique for legacy code, and you will probably mark several. Today we will use Approvals for new development work.

### Introducing the Lift Kata

There is some starting code for doing this Kata with an Approvals approach on [my github](https://github.com/emilybache/Lift-Kata/). Have people read the README file and particularly the explanation of the printer. Make sure everyone has the starting code set up on their machines and the tests pass.

### Concept - scenario and sketch
If you already did a learning hour on discovery and formulation of scenarios for this kata, get people to bring out their formulations. Otherwise, sketch on a whiteboard a simple scenario. For example "Idle lift fulfills request." You might have a formulation that looks like this:

   
	1      *  1
	0     [A] 0

	...

	1    [*A] 1
	0         0

	...

	1     ]A[ 1
	0         0

### Concrete
Do the lift kata in pairs

### Reflect
Pick a couple of pairs and ask them to put their test code up on the screen. Compare the test code to the scenario formulation they started with. Do they look the same?


