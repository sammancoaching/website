---
theme: refactoring
title: Idiomatic Code
kata: theatrical_players
difficulty: 2
author: emilybache
affiliation: ProAgile
---

# Idiomatic Code

Whether you find code readable or not can to a large extent depend on whether it uses an idiomatic style that you are used to. Different language communities have different idiom. In this session we look at how to convert non-idiomatic code into something recognizable for that language.

## Learning goals

* describe some idioms for a familiar programming language
* apply refactorings to convert non-idiomatic code into something more readable
* identify some common refactorings that help you to increase readability in any language

## Session Outline
 
* 5 min connect: non-idiomatic code
* 5 min concept: Describe some idioms 
* 35 min do: pairs refactor Theatrical Players
* 5 min reflect: analyze readability


### Connect
Show them some very non-idiomatic code in their language and ask them what's wrong with it.

### Concept
Describe some idioms for the programming language you will be using in the session.

For example

* C - pass the struct as first argument of any function that modifies that struct
* Python - use a. generator instead of a for loop
* Kotlin - use sealed classes instead of an enum
* golang - return x, err where err is nil if everything went well, and the error otherwise

Bring up the code you'll be using in the exercise, and talk about where it is not idiomatic for the language.

### Concrete
Work on a refactoring kata with the explicit aim of making the code readable and idiomatic. Keep a list of names of any refactoring you use. For example work on [Theatrical-Players-Refactoring-Kata](https://github.com/emilybache/Theatrical-Players-Refactoring-Kata)

### Conclusions
Does the code look idiomatic for the language now? Compare your code with that from the other pairs. How is the readability?

