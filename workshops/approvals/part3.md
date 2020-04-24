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
 
* 5 min connect: Behaviour Driven Development - share experiences of it
* 25 min concept: BDD tasks and activities game  
* 10 min concept: explain the Kata and one example
* 20 min concrete: create examples and formulate scenarios in pairs
* 10 min conclusions: present scenarios in groups

(short break)

* 5 min connect: in pairs, properties of a good unit test?
* 20 min concrete: walkabout and assess test snippets  
* 10 min conclusions: best/worst tests? Why?  
* 15 min concept: leap years 2 ways - ordinary TDD and TDD approval testing style   
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

Key aspects of BDD: double loop TDD. Do some 'Discovery' and 'Formulation'.

### Connect: Behaviour Driven Development - share experiences of it

In pairs, tell the other person what you already know about BDD. Have you done it? Sort people into small groups so that hopefully someone in each group knows something about BDD.

### Concept: BDD tasks and activities game  

This activity is described [here](../../exercises/games/bdd_tasks_activities.html)

Explain the inner loop is the ordinary Red-Green-Refactor loop that we have in TDD. The outer loop is Failing scenario - Passing scenario - Refactor. The rhythm of the outer loop is slower. A scenario exercises a thicker chunk of code than a unit test. A scenario is understandable by everyone in the team, including business representatives.

### Concept: explain the Kata and one example

Explain the Lift Kata and show the list of [requirements](../../exercises/kata_descriptions/lift.html). You can act as the business representative if they have questions about the requirements. 

Come up with an example, note it on a whiteboard where everyone can see. Formulate it into a scenario and also write that on the whiteboard. I think this exercise is particularly suitable for formulating scenarios as sketches and then doing Approval testing.

### Concrete: create examples and formulate scenarios in pairs

In small groups or pairs, get people to come up with more examples and formulate them as scenarios that could be automated. 

### Conclusions: present scenarios in groups

Get small groups to present their examples and formulations to one another. 

## Part 2

What do good test cases look like, can approval tests be good test cases.

### Connect: in pairs, properties of a good unit test?

In pairs, write down a list of criteria you could use to assess a unit test you were shown. What are some important design considerations?

### Concrete: walkabout and assess test snippets 

I have gathered together some test cases in the [Lift-Kata-Sample-Tests repo](https://github.com/emilybache/Lift-Kata-Sample-Tests). Have the pairs walk around the room looking at the code snippets you've pinned up on the walls. Have them read the code and try to work out what the test is doing. Assess the test against the criteria they just came up with. Add new criteria as it occurs to them.

Encourage people to circulate and not spend too long on one code snippet. Tell them it's ok to not understand everything about the code, it could be a sign that it has room for improvement.

The idea of the code snippets is that in your judgement, some are better than others. Some are short, some are long, some contain loops, some have too much detail, some have multiple asserts, some use unfamiliar test frameworks, etc.

### Conclusions: best/worst tests? Why? 

When everyone has been looking at the code for about 15-20 minutes, bring it back to whole group discussion. At a flipchart or whiteboard, ask people to volunteer what they've learnt. You want to know the criteria they came up with, and which test snippets on the wall are the best/worst. You might find disagreement in the group which could be interesting to know but possibly not helpful to have a big discussion about in a whole group. Try to focus on what people agree on.

### Concept: leap years 2 ways - ordinary TDD and TDD approval testing style 

Show the plain vanilla TDD implementation of Leap Years first. Don't forget the first step, which is writing up the four test cases on the whiteboard. Implementing the whole Kata only takes a few minutes, and they will probably have seen it before in a previous session. Show it to them again so they remember better.

Start over from scratch and demo another testing style. For ideas about what testing styles you could show, see my repo of [LeapYearTestExamples](https://github.com/emilybache/LeapYearTestExamples).

Since LeapYears is a relatively small problem to solve, probably any other approach than standard TDD looks like overkill. You might want to explain that people should focus on what the approach looks like rather than whether it is appropriate for this problem. You're using a problem they are familiar with so they can focus on something else.

### Conclusions: pairs assess demo tests against their list

Ask people to discuss in pairs. Do the tests that come from the new approach have all the properties they came up with during the earlier part of the session? Leave your demo code up on the projector screen where they can see it while they discuss.

## Part 3

Can we make the tests we formulated earlier into automated tests

### Connect: choose a scenario and sketch 

There is some starting code for doing this Kata with an Approvals approach on [my github](https://github.com/emilybache/Lift-Kata/). Have people read the README file and particularly the explanation of the printer. Make sure everyone has the starting code set up on their machines and the tests pass.

Look at the formulated test cases we made earlier. Choose one to work on automating.

### Concrete: pair on Lift Kata  

Have people automate a formulated test case in [this codebase](https://github.com/emilybache/Lift-Kata/). They should work in pairs

### Conclusions: compare test cases to sketch

Pick a couple of pairs and ask them to put their test code up on the screen. Compare the test code to the scenario formulation they started with. Do they look the same?

## Part 4

Domain Specific Languages

### Concept: Domain Specific Languages

TODO: examples

### Concrete: Sketching scenarios in a DSL

TODO: example scenarios to sketch

### Conclusions: walkabout posters & code review

Get people to look through everything we've done today and discuss with someone what they've learnt. Write answers on the mind-map as sub-nodes.  TODO: mindmap

### Retrospective: gather observations

What are you taking away with you today? TODO: better retrospective format
