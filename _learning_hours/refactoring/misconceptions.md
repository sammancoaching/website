---
theme: refactoring
title: Misconceptions about Refactoring
kata: tennis
difficulty: 1
---


# Misconceptions about Refactoring

In this session we talk about what refactoring is and why we do it. We work on improving some names to improve readability.

## Session Outline

* 15 min connect: refactoring warm-up questions   
* 5 min concept: When should you refactor
* 30 min do: pairs refactor Tennis3
* 5 min reflect: review warm-up questions


### Discuss Misconceptions
Create a handout with a number of statements about refactoring, which are controvertial, wrong, or only partially true. Ask people to discuss them in small groups and decide whether each statement is true or false. [Here](/exercises/warm_up_questions/refactoring_warm_up_questions.html) is a sample page of questions you could use.

### Purpose of refactoring
Remind people that the purpose of refactoring is to make code easier to understand and cheaper to modify. 

It's a necessary part of iterative and incremental development. You don't plan the entire design up front, you take working code and change the design to support new functionality. 

Another use of refactoring is for code that has technical debt, that is, it is harder than necessary to understand and modify. You do a series of safe refactorings on it to improve readability and reduce complexity.

### Work on Tennis3
Examine the code in Tennis3 in [The Tennis Refactoring Kata](https://github.com/emilybache/Tennis-Refactoring-Kata). Is there anything wrong with this code? Do you see any technical debt? How could refactoring improve it? Discuss what's needed and address problems one by one.

### Reflect
Have people note down an answer to this question: When should you refactor?
