---
layout: default
title: Extract Function, Tennis
parent: Refactoring
grand_parent: Learning Hours
nav_order: 1
---

# Extract Function Refactoring in Tennis1

It's useful to have a vocabularly for talking about refactoring. It will help you to communicate when doing strong-style pairing or mob programming. In this learning hour we'll learn what refactorings are and the names of some of them. We'll also practice applying Extract Function in order to address a Long Function smell.

## Session Outline
 
* 5 min connect: collect names of refactorings   
* 5 min concept: Martin Fowler's refactoring definitions
* 10 mins do: review Tennis and suggest refactorings   
* 10 min demo: Extract function on Tennis1 
* 25 min do: pairs refactor Tennis1 
* 5 min reflect: own definition of refactoring

### Names of Refactorings
Have people note down names of refactorings that they know already.

### Refactoring definition
Put up Martin Fowler's definitions of Refactoring as a noun and verb on a projector screen or write them on a flipchart. Explain how you understand these definitions. You could point out the code shouldn't break while you refactor, and the reason to refactor is primarily economic not moral. You could mention that as you refactor you take a series of small steps and can commit and share your work after any completed step.

### Review code
Have them review the code in "Tennis1" in [The Tennis Refactoring Kata](https://github.com/emilybache/Tennis-Refactoring-Kata), and think about what refactorings they might want to apply to this code. The idea is just to read the code at this point, not change it.

When they've looked at the code, go through their suggestions. Tell them the 'official' name (from Fowler's book) if they don't know what the refactoring is called.

### Extract function
The implementation for Tennis1 has a Long Function smell. Demonstrate how to use Extract Function to split it into parts. I suggest three functions for 'equal score', 'endgame' and something you could perhaps call 'early game'. Use IDE refactoring tools if you have them and if so get someone to write on a whiteboard the key combinations you are using. 

Stop refactoring when the public 'score' method looks short and has improved readability. There will still be other code smells, leave them for another time. For the moment we are focussing on Extract Function. We have done enough to make a difference.

### Do refactoring
Have them do what you just showed them. If they have time, they can carry on and refactor away more code smells.

### Define 'Refactoring'
How would you define 'refactoring'? Write a definition on a sticky note and take it with you to put next to your screen.
