---
theme: testable_design
title: Testing Private Methods
kata: yatzy
difficulty: 2
author: emilybache
affiliation: ProAgile
tags: testable_design
---

Testing Private Methods with Yatzy
------------------------------------

How should you test private methods? That's the main question we'll be looking at in this learning hour. We'll be working with the Yatzy kata since people will hopefully discover you need one or more private methods in order to solve it. It's useful if the group has worked on this exercise before. You want them to get far enough with it that they implement one or more private methods.

The main learning point for this session is that when we do TDD, there are some strategies for testing private methods that we probably won't use. For example we don't need to use reflection or a PowerMock tool to break encapsulation in order to get at a private method to test it. TDD will help us to choose a testable design. Those other strategies are ones we may choose when faced with code that was not designed for testability.

## Session Outline
 
* 5 min connect: pairs discuss how to test private methods  
* 10 min concept: private method strategies   
* 40 min do the kata 
* 5 min reflect: which strategies did we use 

### Connect
In pairs, come up with strategies for how to test private methods. Have them write them on post-it notes.

### Concept
Prepare a flipchart paper with the question "How do you test private methods". Make it look nice with a doodle of a stop sign or similar.
Invite pairs to come forward and present one of their strategies then stick their post-it to the flipchart. Write additional text next to it if the post-it is vague. If the group runs out of strategies and you can think of more, add your own ideas to the list.

### Do - work in pairs or a mob to implement Yatzy
Have them work in pairs to test-drive an implementation in a programming language they know. There are several opportunities for private methods. The main public entry point is a function that takes a category and five dice, and returns a score. It will probably call private functions for calculating each strategy.

Another opportunity for private functions is when they find several category score functions are similar and can re-use some logic. For example you could have a function that calculates the frequencies of each dice. This is what that function could look like in python:

	def frequencies(dice):
		frequencies = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}
		for die in dice:
			frequencies[die] += 1
		return frequencies
 
Ask leading questions to help people realize they need private methods, and help them choose good strategies to test them.

### Reflect
- On the flipchart showing the strategies for testing private methods, make a mark by the strategies each pair used.
- Did everyone choose the same strategy? Ask a couple of people to explain their choices.
- Did using TDD affect the choice of strategy?

Hang the flipchart somewhere in the team area after the session.

