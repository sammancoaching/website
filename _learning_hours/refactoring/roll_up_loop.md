---
theme: refactoring
title: Roll Up Loop
kata: timer_expiry
difficulty: 3
author: emilybache
affiliation: ProAgile
tags:  refactoring
---

# Roll Up Loop

This refactoring doesn't seem to have an official description anywhere, but it's one I often use. The sign it could be useful is a long method with a series of similar code paragraphs or if statements, where each paragraph essentially calculates or updates a value of the same type. 

A loop is really just a sequence of blocks each doing the same thing, so often you can make this kind of code cleaner and easier to read by rolling up the sequence of code blocks into a loop. The trick is to identify an abstraction to loop over.

## Learning Goals

* Describe the design feedback indicated by a sequence of similar statements or repeating blocks.
* Identify an abstraction to loop over in order to remove duplication in a sequence of similar statements or repeating blocks.

## Session Outline

* 5 min connect: Review code for smells and duplication 
* 15 min concept: Roll-up loop
* 25 min do: refactor to roll up the loop
* 5 min reflect: review refactored code & note down learnings

## Connect: Code smells and refactorings

Ask the group to review the code for the exercise you will do later on. I've used several different ones depending on how skilled the group is. The idea at this point is to get them to read the code with enough detail that they see the long method and within that several similar code paragraphs.

## Concept: Roll Up loop
Explain what this is through examples. I have quite a few examples in [RollUpLoop-Refactoring-Practice](https://github.com/emilybache/RollUpLoop-Refactoring-Practice). Put the 'before' version on a slide or handout and hide the 'after' version for the moment. Give them a series of 6-10 examples to go through and for each one ask the question: "Imagine turning the sequence into a loop. What type would you loop over?"

The main skill here is being able to see how the similar code paragraphs could be rolled up into a loop if you found a suitable type to loop over. A key insight is that for some of them the type is already there in the code, but for the harder examples that type doesn't exist yet.

Once everyone has had a chance to look through the examples and come up with a type to loop over, reveal the 'after' versions of the code and go through them together. Make sure everyone can see the duplication 'before' and that the 'after' version is shorter and easier to read. (If it's not, then the learning is that code smells don't always indicate a design problem you can fix).

## Concrete: refactoring practice
Depending on their skill level, choose a suitable exercise. You could simply have them work through one of the harder examples in [RollUpLoop-Refactoring-Practice](https://github.com/emilybache/RollUpLoop-Refactoring-Practice) turning the 'before' version into the 'after' version. Encourage them to continue refactoring after that if they now see new opportunities to use any abstractions they have introduced.

For a follow-up session or harder exercise, try [TimerExpiry](https://github.com/emilybache/TimerExpiry-Refactoring-Kata) or [ClarifyException](https://github.com/emilybache/Clarify-Exception-Refactoring-Kata) or [BuildPipeline](https://github.com/emilybache/BuildPipeline-Refactoring-Kata). For these exercises there is no 'after' shown in the main branch. 

For TimerExpiry you could change to a design with a list of function pointers you loop over. Each function returns the time until the timer goes off. Then find the smallest value in one place rather than 6 places. 

For ClarifyException you can have a small class rather than a function pointer - with two methods "matches" and "build".

For BuildPipeline you can ask them to create a 'PipelineStep' interface with three concrete implementatons to loop over - TestStep, DeployStep and ReportStep.

## Conclusions: note down learnings
Review the code each group has come up with and how much better it looks now. As a short final conclusion you could ask people to note down in their own words "If you have a series of similar statements or blocks of code in a method, what steps could you take to refactor it?"
