---
theme: testable_design
title: Overdesign
kata: fizzbuzz
difficulty: 1
author: emilybache
affiliation: ProAgile
---

FizzBuzz - how does TDD affect your design?
---------------------------------------------------

You can write a FizzBuzz implementation in a handful of lines of code. At the other end of the scale I was fascinated to see this repo ["FizzBuzz Enterprise Edition"](https://github.com/EnterpriseQualityCoding/FizzBuzzEnterpriseEdition), which is genuis. It's _biting_ satire and of course you would never write anything as bad as that. Of course not! 

In this learning hour we'll use FizzBuzz to have a discussion about how TDD affects your design. Hopefully they will realize TDD helps you to get a testable design, and avoid overdesign. 

It's probably a good thing if the participants have done FizzBuzz before. It's good if they know TDD well enough to finish an implementation in the allotted time.

## Session Outline

* 5 min connect: pairs discuss experience with overdesign  
* 15 min concept: walk and talk about code samples 
* 5 min show choices  
* 20 min do: fizzbuzz in pairs 
* 5 min pairs compare actual code with samples

### Connect
Find a pair to work with today. Discuss whether the code you usually work with suffers from overdesign or if it could benefit from more structure and abstractions.

### Concept
Print out and pin up the code samples from ["FizzbuzzKata-Samples"](https://github.com/emilybache/FizzBuzzKata-Samples) around the walls of the room, in order. Only include the implementations, not the tests. Have people walk around in their pairs and study the code together. Ask them to consider the following questions:

- If you were to implement FizzBuzz, which of these implementations would your code end up most similar to?
- If you were to implement FizzBuzz **using Test-Driven Development**, which of these implementations would your code end up most similar to?

When the time is up, ask them to stand next to the code sample they would answer for the first question. Note if there are any clusters. Then ask them to move and stand next to the code sample they would answer for the second question. Note if there are new clusters. Pick a couple of pairs at random, some people who moved between questions and people who stayed still. Ask them to explain their reasoning.

### Do
Have the group work in pairs to implement [FizzBuzz]({% link _kata_descriptions/fizzbuzz.md %}) using TDD.

### Reflect
- Show your implementation code to another pair. Ask them which code sample it is most similar to. Is that what you expected?
- Swap roles and tell the other pair which code sample you think is most similar to their implementation.
- Can you conclude anything about how TDD affects the way you design code?


