---
theme: code_reading
title: Code Reading - Identifying Code Smells
kata: gilded_rose
difficulty: 1
author: emilybache
---

# Code Smells - Introduction

It's useful to have a vocabulary for talking about refactoring. It will help you to communicate when doing strong-style pairing or mob programming. Code smells is perhaps a less-known concept than refactoring and knowing these names will also help you to communicate about code, and identify targets for refactoring. In this learning hour we'll talk about what a code smell is and learn the names of some common ones. 

## Learning Goals
* Describe the term "Code Smell"
* Use 'Scanning' to find the 'Long Method' code smell quickly
* Remember you can use 'Extract Method' to make a long method shorter

## Session Outline
 
* 5 min connect: How do you know when you have bad code? 
* 10 min concept: Martin Fowler's code smell definition 
* 10 min concrete: Sparrow deck on Long Methods
* 20 min concrete: Code Reading practice exercise
* 10 min demo: Fixing Long Method with Extract Method
* 5 min reflect: Describe code smell in your own words

### How do you know when you have bad code?
Have you ever encountered bad code? If so, what characteristics does it have? Discuss in pairs and note down "bad code" characteristics. Note down your ideas and share them with the group when the facilitator asks.

If someone claims there is no such thing as bad code, try not to get into a big argument. It's a valid perspective but not actually very useful. Try to get the discussion more onto code smells as a concept and ask them to suspend their disbelief in bad code for the duration of the session.

### Code smells
Explain Martin Fowler's [description of code smells](https://www.martinfowler.com/bliki/CodeSmell.html). The list of [Code Smells](/reference/code_smells/index.html) on this site uses the same names as Martin Fowler's book 'Refactoring'. There is another list of common code smells on [wikipedia](https://en.wikipedia.org/wiki/Code_smell). If they have already met some code smells in a previous session, remind them of the descriptions of those.

### Sparrow deck on Long Methods
If they havn't seen a sparrow deck before, show them the original either using [Llewellyn's slides](https://llewellynfalco.blogspot.com/p/sparrow-decks.html) or [Emily's video](https://youtu.be/tkqZDaw-4E4). Then show them the "Long Methods" sparrow deck.

### Code Reading practice
This exercise is explained on the [code reading exercise]({% link exercises/code_reading.md %}) page. First demonstrate how to do it on the [Tennis Refactoring Kata](https://github.com/emilybache/Tennis-Refactoring-Kata). Then ask them to do the same for the [Office Cleaner Robot Refactoring Kata](https://github.com/sammancoaching/OfficeCleaningRobot-Refactoring-Kata).

This is a [Individual work with showcasing]({% link _activities/concrete/individual_work_with_showcasing.md %}) exercise. Consider putting everyone in individual breakout rooms with a time limit of 5 minutes. They can return to the main room sooner if they are finished quickly. My experience tells me most people can scan all 12 code samples in around 2-3 minutes.

### Discussion
Get everyone to share their results: 

* How long did they spend reading the code (if less than the 5 minute limit) 
* Which code samples had a long method 

Discuss whether this sparrow deck and exercise has helped them to read code better.

### Demo - Extract Method
An important aspect of code smells is that when you detect one, it gives you a clue about what refactorings to apply to fix it. For Long Method you can usually make things better by using Extract Method. This effectively lets you reduce the complexity you have to hold in your head at the same time by using 'chunking'. You are replacing a section of code with a named function so many lines of code turn into only one thing you need to remember. Of course if the section you extract and name doesn't make sense then you don't get this complexity reduction effect.

Explain this and show a demo of using "Extract method" to address a Long Method smell. For example version 9 of the [Office Cleaner Robot Refactoring Kata](https://github.com/sammancoaching/OfficeCleaningRobot-Refactoring-Kata). The long method contains a switch statement and each case can be extracted to a method like "MoveNorth" etc.

### Conclusions - Code Smells main idea
If you had to explain the main idea of Code Smells to a colleague, what would you say?

This is an [explain the main idea]({% link _activities/conclusions/explain_main_idea.md %}) conclusions activity.

