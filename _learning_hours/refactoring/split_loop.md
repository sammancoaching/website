---
theme: refactoring
title: Split Loop
name: split_loop
code_smell: shotgun_surgery
kata: theatrical_players
difficulty: 2
author: emilybache
---

# Split Loop (simpler version)

Merge conflicts are a major cause of bugs - people get in each other's way when they are editing the same lines of code because the same section of code does more than one thing.  It would be better to split up the logic according to each responsibility. Today we’re going to look at how to divide it up safely.

## Learning Goals

* Identify situations where a loop has two concerns that could be split.
* Use "Split Loop" to separate concerns into different parts of the code

## Session Outline

* 10 min connect: Classify the code
* 10 min concept: Shotgun Surgery
* 5 min demo: Split Loop
* 35 min do: Split loop in Theatrical Players and Expense Report
* 5 min reflect: When should you use this?

## Connect: Classify the code
Give people copies of the code for [Theatrical Players](https://github.com/emilybache/Theatrical-Players-Refactoring-Kata) in a format they can sketch on, like paper or an online activity board. Give them three colours of pen to mark sections of code that have these concerns:

* Formatting and presentation
* Data transformation and calculation
* Unclear or mixed

Also ask them to think about what design principles this code might break, or if there are any obvious code smells.

When everyone has had a chance to read the code and colour it, gather together and talk about what you found. The code should be stripy - mixed concerns all over the place. People might talk about problems with the Single Responsibility Principle or with Divergent Change. If they don't mention these things, don't worry, you'll explain in the next part.

## Concept: Shotgun Surgery
Explain that the reason you wanted them to classify the code like this is because the next features that will be developed are

* Customer statements in HTML format
* Additional types of play

For each type of change, the impacted lines of code are all over the place. What we'd be doing is a form of [Shotgun Surgery]({% link _code_smells/shotgun_surgery.md %}). This introduces a danger of merge conflicts if the changes are happening at the same time, and also the danger you'll miss somewhere that needs updating. We'd like to refactor the code before we begin either change.

## Demo: Split loop
In Theatrical players show that you need to do several refactorings in order to gather the presentation logic together and separate it from the calculation logic. Show how to do that safely, including [Split Loop]({% link _refactorings/split_loop.md %}). Use the simpler form where you inline all the local variables.

## Concrete Practice: Split loop in Theatrical Players and Expense Report
In pairs, do the same exercise in Theatrical Players that you just demonstrated. When they have done that one, they could try [Expense Report](https://github.com/emilybache/ExpenseReport-Refactoring-Kata) which is very similar.

## Conclusions: When should you use this?
[When should you use this?]({% link _activities/conclusions/when_to_use_this.md %}) What would prompt you to try 'split loop'? Everyone note down what they would look for.
