---
theme: refactoring
title: Vocabulary for Refactoring
kata: tennis
difficulty: 1
author: emilybache
---

# Vocabulary for Refactoring

It's useful to have a vocabularly for talking about refactoring. It will help you to communicate when doing strong-style pairing or mob programming. In this learning hour we'll learn what refactorings are and the names of some of them. We'll also practice applying Extract Function in order to address a Long Function smell.

## Learning Goals

* Remember the name of the refactoring "Extract Function" aka "Extract Method"
* Identify a situation when you can successfully apply "Extract Function" or "Extract Method"

## Session Outline
 
* 5 min connect: collect names of refactorings   
* 5 min concept: Martin Fowler's refactoring definitions
* 10 mins do: review code and suggest refactorings   
* 10 min demo: Extract function
* 25 min do: pairs refactor
* 5 min reflect: own definition of refactoring

### Names of Refactorings
Have people note down names of refactorings that they know already. For example, suggest they already know "Rename variable"

### Refactoring definition
Put up [Martin Fowler's definitions](https://martinfowler.com/bliki/DefinitionOfRefactoring.html) of Refactoring as a noun and verb on a projector screen or write them on a flipchart. Explain how you understand these definitions. You could point out the code shouldn't break while you refactor, and the reason to refactor is primarily economic not moral. You could mention that as you refactor you take a series of small steps and can commit and share your work after any completed step.

### Review code
Have them review some code that has a smell that would indicate an 'Extract function' (aka 'Extract method') refactoring would help. For example it has a long method or some obvious duplication. The idea is just to read the code at this point, not change it. Ask them to note down any parts of the code they'd like to refactor. It doesn't matter if they don't know the official name of the refactoring, most people can describe what they mean.

Example katas that work well:

* Tennis1 in [The Tennis Refactoring Kata](https://github.com/emilybache/Tennis-Refactoring-Kata),
* [Theatrical Players Refactoring Kata](https://github.com/emilybache/Theatrical-Players-Refactoring-Kata).

When they've looked at the code, go through their suggestions. Help them learn the 'official' name (from Fowler's book, or refactoring tool menus) if they don't know what the refactoring is called. Hopefully they will have mentioned 'Extract Function' as one of their suggestions. If not, point it out. 

### Extract function
Demonstrate how to use Extract Function on the code they just reviewed. Use IDE refactoring tools if you have them and if so get someone to write on a whiteboard the key combinations you are using.

* Tennis1: I suggest three functions for 'tie', 'endgame' and something you could perhaps call 'early game'. 
* Theatrical Players: Extract a function for 'amountFor' and 'volumeCredits' as suggested in Fowler's book.

Don't refactor everything, just demo one or two extract functions. There will still be other code smells, leave them for later. For the moment we are focussing on Extract Function.

### Do refactoring
Have them do what you just showed them. If they have time, they can carry on and refactor away more code smells.

### Define 'Refactoring'
How would you define 'refactoring'? Write a definition on a sticky note and take it with you to put next to your screen.
