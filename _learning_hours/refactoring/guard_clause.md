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
It is often caused by many conditions or loops that are deeply nested.
There are many ways to simplify such complicated code.
A common one that is sometimes applicable is to [Replace Nested Conditional with Guard Clauses](https://refactoring.com/catalog/replaceNestedConditionalWithGuardClauses.html).

## Learning Goals

* Being able to identify the "Bumpy Road" code smell.
* Understand the "Guard Clause" concept.
* Simplify nested conditionals by replacing them with guard clauses.

## Session Outline
 
* 5 min connect: Discuss: How much nesting inside a function is tolerable?  
* 10 min concept: Demo the refactoring
* 5 min conclusion: Compare the original code with the simplified version
* 35 min concrete practice: Practice the same refactoring
    * In an ensemble
    * In pairs
* 5 min conclusion: Come up with places in your code where this would apply

### Connect: How much Nesting is tolerable?
Have people discuss in pairs how much levels of nesting they think is ok.

### Concept: Demo the Refactoring
A small code to practice the *Replace Nested Conditional with Guard Clauses* refactoring is the [PayRoll-Refactoring-Kata](https://github.com/gregorriegler/payroll-refactoring-kata). 
A good way to start is by asking the participants whether they see any issue with this code.
Next you want to explain what the "Bumpy Road" code smell is using the given code.
Then, demo the refactoring slowly and explain your thought process.
First select the `result` variable to show how big its scope is and how often it is used.
Explain that it is a good idea to reduce the scope of such a variable because it reduces cognitive load and allows further refactoring.
Go on showing the refactoring by introducing early returns.

### Conclusion: Compare the original code with the simplified version.
Ask the people whether they think its easier to read and why.

### Concrete Practice: Practice the same Refactoring
Have the participants practice the same exercise.
If the group is familiar with Ensemble Programming, you might want them to do it in an ensemble first.
When there is time left have them do it again in pairs.

### Conclusion: Come up with Places in your Code
Ask the participants whether they know a code in their project where that refactoring would apply, too.