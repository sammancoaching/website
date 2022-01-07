---
theme: refactoring
title: Simplify Conditional
kata: supermarket_receipt
difficulty: 3
author: emilybache
---

# Simplify Conditional

Lean on the good tests. Improve the code in ShoppingCart.

## Session Outline

* 5 min connect: What is the goal of refactoring? 
* 5 min concept: Refactoring conditionals
* 5 min demo: show the patterns and the shape of the refactoring
* 35 min concrete: refactor into simpler conditional structure
* 5 min conclusions: note down learnings

## Connect: What is the goal of refactoring? 

What are you hoping to achieve, when you sit down to refactor some code? What is your motivation?

## Concept: Refactoring conditionals

Examples of behaviour-preserving transformations for conditionals. I started a [repo](https://github.com/emilybache/Refactor-Conditionals) for some of these. 

* De Morgan's law
* Split & join if statements
* Two statements in one if statement -> two if statements (specialization of 'Split Loop')
* redundant 'else' when followed by one more if
* Normalize Conditional

## Demo: show the patterns and the shape of the refactoring

Working on [SupermarketReceipt](https://github.com/emilybache/SupermarketReceipt-Refactoring-Kata). You have several if statements that assign a value to 'x' and several that assign a value to 'discount'. One assigns both. You'd like to do 'split loop' on that if statement. Then you can use 'slide statement' and 'extract method' so you have one method to calculate 'x' and one to calculate the discount.

Explain this plan and note it on the whiteboard.

## Concrete: refactor into simpler conditional structure

Set the group loose on the refactoring. Remind them of the plan, and remind them to use their tools.

## Conclusions: note down learnings

How would you spot other situations where you can use 'split loop', 'slide statement' and 'extract method'?

