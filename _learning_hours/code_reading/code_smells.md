---
theme: code_reading
title: Code Reading - Identifying Code Smells
kata: gilded_rose
difficulty: 1
author: emilybache
affiliation: Praqma
---

# Code Reading - Identifying Code Smells

It's useful to have a vocabulary for talking about refactoring. It will help you to communicate when doing strong-style pairing or mob programming. Code smells is perhaps a less-known concept than refactoring and knowing these names will also help you to communicate about code. In this learning hour we'll talk about what a code smell is and learn the names of a few of them. 

## Session Outline
 
* 5 min connect: How do you know when you have bad code? 
* 10 min concept: Martin Fowler's code smell names 
* 30 mins do: find code smells
* 5 min reflect: What code smells does your production code often suffer from?

### How do you know when you have bad code?
Have you ever encountered bad code? If so, what characteristics does it have?

Discuss in pairs and note down "bad code" characteristics. If you have never encountered bad code, note down why you think that is.

Note down your ideas and share them with the group when the facilitator asks.

### Code smells
Explain Martin Fowler's [description of code smells](https://www.martinfowler.com/bliki/CodeSmell.html). The list of [Code Smells](/reference/code_smells/index.html) on this site uses the same names as Martin Fowler's book 'Refactoring'. There is another list of common code smells on [wikipedia](https://en.wikipedia.org/wiki/Code_smell). Go through some of the descriptions of the most common smells they are likely to encounter.

### Find code smells
Have them review some code and note down any code smells they find. The idea is just to read the code and identify smells, not do anything about it. Note that you can identify code smells without necessarily understanding the code or being able to safely change it.

Example katas that work well:

* Tennis1, Tennis2 or Tennis3 in [The Tennis Refactoring Kata](https://github.com/emilybache/Tennis-Refactoring-Kata)
* [Theatrical Players Refactoring Kata](https://github.com/emilybache/Theatrical-Players-Refactoring-Kata).
* [Gilded Rose Refactoring Kata](https://github.com/emilybache/GildedRose-Refactoring-Kata)

When they've looked at the code, write up on a whiteboard the names of smells that they have found. Tell them the 'official' name (from Fowler's book) if they don't know it. Repeat with another code sample.

You are hoping that they will find smells like these:

* Tennis1: [Long method](/code_smells/long_function.html)
* Tennis2: [Duplicated code](/code_smells/duplicated_code.html)
* Tennis3: [Mysterious names](/code_smells/mysterious_name.html)
* Theatrical Players: [Primitive Obsession](/code_smells/primitive_obsession.html), [Comments](/code_smells/comments.html)
* Gilded Rose: [Long function](/code_smells/long_function.html), [Heavy indentation](/code_smells/heavy_indentation.html)

### What code smells does your production code often suffer from?
Are there any particular smells that are common in your production code? Note down their names and share with the group. If other people working in the same codebase as you have different ideas, also note them down. Keep the names of these code smells on a note by your computer, so you'll be reminded to watch out for them and perhaps even fix them. 
