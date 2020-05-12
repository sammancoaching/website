---
layout: default
title: Behaviour Driven Development with Approval tests
parent: Approval Testing
grand_parent: Workshops
nav_order: 3
---

# Using Approval Testing in Behaviour Driven Development

Typically people use a Gherkin-syntax tool like Cucumber for BDD, but here we will explore scenarios and set up test cases with an approval testing approach. We look at the key aspects of BDD: 

- Discovery
- Formulation
- Automation

and how each is affected by choosing an Approval testing approach.


We will go through a worked example in small groups and practice doing BDD with an approval testing approach. Each group can agree which programming language to use for the automation part, with a choice of Java, C#, Python, C++ and Go. 


## Session Outline
 
* 5 min connect: in pairs, properties of a good unit test?
* 20 min concrete: walkabout and assess test snippets  
* 10 min conclusions: best/worst tests? Why?  
* 10 min demo: Leap Years TDD

(short break)

* 5 min connect: Behaviour Driven Development - share experiences of it
* 25 min concept: BDD tasks and activities game  
* 20 min concept: what is BDD
* 5 min conclusions: Note down how BDD would differ with Gherkin or approval tests

(short break)

* 5 min connect: How does a lift work? Explain to another person
* 5 min concept: Formulating a lift DSL
* 20 min concrete: create examples and formulate scenarios in pairs
* 10 min conclusions: present scenarios in groups
* 5 min conclusions: pairs assess demo tests against their list

(short break)

* 10 min concept: choose a scenario and sketch 
* 45 min concrete: pair on Lift Kata  
* 5 min conclusions: compare test cases to sketch

(short break)

* 5 min concept: Domain Specific Languages
* 15 min concrete: Sketching scenarios in a DSL
* 10 min conclusions: walkabout posters & code review
* 15 min retrospective: gather observations

## Part 1

What do good test cases look like, can approval tests be good test cases.

### Connect: in pairs, properties of a good unit test?

In pairs, write down a list of criteria you could use to assess a unit test you were shown. What are some important design considerations?

### Concrete: walkabout and assess test snippets 

I have gathered together some test cases in the [Lift-Kata-Sample-Tests repo](https://github.com/emilybache/Lift-Kata-Sample-Tests). Have the pairs walk around the room looking at the code snippets you've pinned up on the walls. Have them read the code and try to work out what the test is doing. Assess the test against the criteria they just came up with. Add new criteria as it occurs to them.

Encourage people to circulate and not spend too long on one code snippet. Tell them it's ok to not understand everything about the code, it could be a sign that it has room for improvement.

The idea of the code snippets is that in your judgement, some are better than others. Some are short, some are long, some contain loops, some have too much detail, some have multiple asserts, some use unfamiliar test frameworks, etc.

### Conclusions: best/worst tests? Why? 

When everyone has been looking at the code for about 15-20 minutes, bring it back to whole group discussion. At a flipchart or whiteboard, ask people to volunteer what they've learnt. You want to know the criteria they came up with, and which test snippets on the wall are the best/worst. You might find disagreement in the group which could be interesting to know but possibly not helpful to have a big discussion about in a whole group. Try to focus on what people agree on.

### Concept: leap years with TDD

Show the plain vanilla TDD implementation of Leap Years first. Don't forget the first step, which is writing up the four test cases on the whiteboard. Implementing the whole Kata only takes a few minutes, and they will probably have seen it before in a previous session. Show it to them again so they remember better.

## Part 2

Key aspects of BDD: double loop TDD. Do some 'Discovery' and 'Formulation'.

### Connect: Behaviour Driven Development - share experiences of it

In pairs, tell the other person what you already know about BDD. Have you done it? Sort people into small groups so that hopefully someone in each group knows something about BDD.

### Concept: BDD tasks and activities game  

This activity is described [here](../../exercises/games/bdd_tasks_activities.html)

Explain the inner loop is the ordinary Red-Green-Refactor loop that we have in TDD. The outer loop is Failing scenario - Passing scenario - Refactor. The rhythm of the outer loop is slower. A scenario exercises a thicker chunk of code than a unit test. A scenario is understandable by everyone in the team, including business representatives.

### Concept: explain BDD "centered community"

Include demos of Cucumber BDD and Approvals BDD. Concept of centered community.

### Conclusions: Note down how BDD would differ with Gherkin or approval tests

Write sticky notes - perhaps on your BDD diagram.

### Connect: How does a lift work? Explain to another person

Discuss what user stories you can think of based on own experience.

### Concept: formulation with DSL

Explain the DSL we'll be using for this exercise

### Concrete: create examples and formulations

Explain the Lift Kata and show the list of [requirements](../../exercises/kata_descriptions/lift.html). You can act as the business representative if they have questions about the requirements. 

In small groups or pairs, get people to come up with examples and formulate them using the DSL.

### Conclusions: present scenarios in groups

Get small groups to present their examples and formulations to one another. 

### Conclusions: pairs assess demo tests against their list

Ask people to discuss in pairs. Do the tests that come from the new approach have all the properties they came up with during the earlier part of the session?

## Part 3

Can we make the tests we formulated earlier into automated tests

### Connect: choose a scenario and sketch 

There is some starting code for doing this Kata with an Approvals approach on [my github](https://github.com/emilybache/Lift-Kata). Have people read the README file and particularly the explanation of the printer. Make sure everyone has the starting code set up on their machines and the tests pass.

Look at the formulated test cases we made earlier. Choose one to work on automating.

### Concrete: pair on Lift Kata  

Have people automate a formulated test case in [this codebase](https://github.com/emilybache/Lift-Kata). They should work in pairs

### Conclusions: compare test cases to sketch

Pick a couple of pairs and ask them to put their test code up on the screen. Compare the test code to the scenario formulation they started with. Do they look the same?

## Part 4

Domain Specific Languages

### Concept: Domain Specific Languages

Ask them to search the internet for examples of Domain Specific Languages. They should find things like:

* Regular Expressions
* plantUML
* SQL
* Musical Notation
* Gherkin

### Concrete: Sketching scenarios in a DSL

Give scenarios to groups and ask them to sketch one or two test cases for each scenario

* 10-pin bowling scores
* Tic-Tac-Toe
* Conway's Game of Life
* Minesweeper

### Conclusions: walkabout posters & code review

Get people to look through everything we've done today and discuss with someone what they've learnt. Write answers on the mind-map as sub-nodes. Mindmap statements

* Why is readability important in test design?
* What is a Domain Specific Language?
* How do you determine if someone is a member of the BDD community?
* How is BDD different when using Approvals compared with Gherkin?
* What should you keep in mind when formulating a scenario?
* What are the main elements of a BDD process?

### Retrospective: gather observations

What are you taking away with you today? TODO: better retrospective format
