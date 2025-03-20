---
theme: refactoring
title: Change Signature
kata: yatzy
difficulty: 2
author: emilybache
affiliation: ProAgile
---

# Change Signature

Let's practice using this refactoring, especially if refactoring tools are new to the team.

There is a video and other materials available for this learning hour as part of a [Technical Coaching Programme]({% link training/full_package.md %})

## Learning Goals

* describe what the "Change Signature" refactoring does
* Use the "Change Signature" refactoring to harmonize many function to have the same signature
* Judge when the automated tool will save time and effort over doing it by hand

## Session Outline
 
* 5 min connect: Names of refactorings 
* 5 min concept: Change signature 
* 10 min do: review Yatzy and explain exercise
* 30 mins do: Yatzy refactoring   
* 5 min reflect: When would using the refactoring tool be worth it?

### Connect: names of refactorings

Ask the group to list the names of some refactorings they already know. For example they might say Extract Function and Rename variable. Give them only a couple of minutes, depending on experience they might come up with only 1-2 or perhaps 5-6. 

By having them think about refactorings they already know, you get them ready to learn about Change Signature. If someone already mentions it then ask them to describe it - they can do the 'Concept' section for you :-)

### Concept: Change Signature

Explain this refactoring. Perhaps refer to the online documentation for your refactoring tool - for example [IntelliJ](https://www.jetbrains.com/help/idea/change-signature.html). 

### Do: review Yatzy and explain exercise

Show the group the code for the [Yatzy-Refactoring-Kata](https://github.com/emilybache/Yatzy-Refactoring-Kata). Ask them to spend a few minutes reviewing it individually. They should look for any code smells or problems in the code.

Bring the code up on the shared screen and go through the problems they identified. There are many problems in this code, but hopefully someone will mention how inconsistent all the methods are. The names of the parameters are different in every method. What types each method takes are also inconsistent. Explain that you'd like to fix this by using the Change Signature refactoring.

Give the instructions for the exercise: they should begin by making all the various scoring methods (chance, pair, ones, full_house etc) have the same signature. You can tell them which signature you want - I usually mention that "fours" has a good signature - or you can ask them to decide for themselves. So long as they are aiming for consistency and they are using the tools to do Change Signature then that's fine.

### Do: Yatzy

Facilitate the group working in pairs, doing this refactoring.

### Reflect: how did it go
Ask people to reflect on what it was like using the "Change Signature" refactoring tool. In what situations would you use it?

They could write their answers on a note for themselves or in a shared document, or they could discuss in pairs.

Note: this is a [When should you use this]({% link _activities/conclusions/when_to_use_this.md %}) activity.
