---
theme: refactoring
name: guard_clause
title: Replace Nested Conditional with Guard Clauses
kata: payroll
difficulty: 1
author: gregorriegler
---

# Replace Nested Conditional with Guard Clauses

Reading a function that has a lot of nesting is hard.
This is also known as the "Bumpy Road" code smell.
It is often caused by many conditions that are deeply nested.
There are many ways to simplify such complicated code.
A common one that is sometimes applicable is to [Replace Nested Conditional with Guard Clauses](https://refactoring.com/catalog/replaceNestedConditionalWithGuardClauses.html).

## Learning Goals

* Being able to identify the "Bumpy Road" code smell.
* Understand the "Guard Clause" concept.
* Simplify nested conditionals by replacing them with guard clauses.

## Session Outline
 
* 5 min connect: Discuss: How much nesting inside a function is tolerable?  
* 10 min concept: Demo the refactoring
* 35 min concrete practice: Practice the same refactoring
* 10 min conclusion: Compare the original code with the simplified version.

### Connect: How much Nesting is tolerable?
Have people discuss in pairs how much levels of nesting they think is ok.

### Concept: Demo the Refactoring
A small code to practice the *Replace Nested Conditional with Guard Clauses* refactoring is the [PayRoll-Refactoring-Kata](https://github.com/gregorriegler/payroll-refactoring-kata). 
Demo the refactoring slowly, step by step and explain your thought process.
First select the `result` variable, show how big its scope is and how often it is used and explain why this is a problem.
Explain that it is typically a good idea to reduce the scope of a variable because it often enables further refactoring.
Go on showing the refactoring by introducing early returns.

### Concrete Practice: Practice the same Refactoring
Have the participants practice the same exercise in pairs.

### Conclusion: Compare the original code with the simplified version.
Ask the people whether they think its easier to read and why.
Also you may ask them whether they know a code where that refactoring would apply.