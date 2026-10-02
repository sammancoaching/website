---
theme: refactoring
title: Simplify Conditional
kata: supermarket_receipt
difficulty: 3
author: emilybache
affiliation: Praqma
tags:  refactoring legacy
---

# Simplify Conditional

Lean on the good tests. Improve the code in ShoppingCart.

## Learning Goals

Generic

* Know different options to simplify conditionals
* Simplify conditionals safely

Specific for 'split loop', 'slide statement' and 'extract method'

* Describe situations when you would use 'split loop', 'slide statement' and 'extract method'
* Use safe refactoring steps in code that's difficult to understand
* Use the refactorings 'slide statement' and 'extract method' appropriately

## Session Outline

* 5 min connect: What is the goal of refactoring?
* 5 min concept: Refactoring conditionals
* 5 min demo: show the patterns and the shape of the refactoring
* 35 min concrete: refactor into simpler conditional structure
* 5 min conclusions: note down learnings

## Connect: What is the goal of refactoring?

What are you hoping to achieve, when you sit down to refactor some code? What is your motivation?

This is an [Open Question]({% link _activities/connect/open_question.md %}) connect.

## Concept: Refactoring conditionals

Examples of behaviour-preserving transformations for conditionals. I started a [repo](https://github.com/emilybache/Refactor-Conditionals) for some of these.

* De Morgan's law
* Split & join if statements
* Two statements in one if statement -> two if statements (specialization of 'Split Loop')
* redundant 'else' when followed by one more if
* Normalize Conditional (aka lift-up conditional)

## Demo: show the patterns and the shape of the refactoring

Working on [SupermarketReceipt](https://github.com/emilybache/SupermarketReceipt-Refactoring-Kata). You have several if statements that assign a value to 'x' and several that assign a value to 'discount'. One assigns both. You'd like to do 'split loop' on that if statement. Then you can use 'slide statement' and 'extract method' so you have one method to calculate 'x' and one to calculate the discount.

Explain this plan and note it on the whiteboard.

## Concrete (optional): Assign smells to code samples 

Similar to [sorting items]({% link _activities/connect/sort_these_items.md %}), show some slides with code smells from Concept part, and let participants assign stickies with names of respective conditional code smells.

## Concrete: refactor into simpler conditional structure

Set the group loose on the refactoring. Remind them of the plan, and remind them to use their tools.

## Conclusions: note down learnings

Generic: What have you learned today?

Specific for the three techniques: How would you spot other situations where you can use 'split loop', 'slide statement' and 'extract method'?
