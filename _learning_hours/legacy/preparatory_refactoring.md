---
theme: legacy
title: Preparatory Refactoring
kata: trivia_preparatory_refactoring
difficulty: 4
author: Ivett Ördög
affiliation: 
languages: C#
tags: [legacy, refactoring]
---

# Preparatory Refactoring

Often, we want to improve our codebase, but refactoring is seen as a non-essential activity that gets postponed. Preparatory refactoring integrates refactoring into feature work: before adding a new feature, we refactor to make the implementation easier. This approach saves time and leads to a cleaner, more maintainable codebase.


## Learning Objectives
- Understand the benefits of refactoring before adding a feature, not after
- Learn to envision the ideal design for a new feature and use this vision to guide refactoring
- Appreciate the value of goal-driven refactoring, tailored to an immediate change

## Prerequisite

This learning hour is based on the Trivia kata, however it assumes tests are already in place and the typo `Answer was corrent!!!!` has been fixed. The Trivia kata is available [here](https://github.com/jbrains/trivia) and is maintained by J.B.Rainsberger.

Before starting:
1. Clone the Trivia repository
2. Ensure you have all necessary dependencies installed

Since the original kata doesn't include tests, you'll need to:
1. Add unit tests for the existing functionality
2. Fix the typo in the "Answer was correct" message
3. Ensure all tests pass before proceeding with the refactoring exercises

## Outline
* 10 min connect: How hard is it to add this feature?
* 5 min connect: How hard is it to add this feature after seeing the code?
* 5 min concept: What is preparatory refactoring? (swamp vs. highway analogy)
* 10 min concrete: Demo for adding customizable categories using preparatory refactoring
* 15 min concrete: Participants try to repeat the steps from the demo
* 5 min reflect: What are the advantages of preparatory refactoring? When should you use it?

### Connect
1. Describe the change request: In the Trivia game, players move around a board, each field has a category, and when they land on a category, they answer a question. Initially, there are four categories; the new requirement is to support six categories.
2. Ask participants: "How hard do you think it is to implement this change if you don’t know the codebase?" Participants share their estimates (e.g., sticky notes on Miro/whiteboard) and discuss.
3. Reveal the actual code, showing the complexity and scattered category logic. Ask again: "How hard is it now?" and discuss how their estimates change.

### Concept
Present Kent Beck’s advice: "Make the change easy, then make the easy change." Use the swamp vs. highway analogy: Badly designed code is like a swamp; instead of slogging through, preparatory refactoring is like walking to the highway and then driving there.

### Concrete (Demo)
- Goal: Isolate a `Questions` class and refactor the code to use a single array of categories.
- A recorded demo is available [here](https://www.youtube.com/watch?v=<TO BE ADDED>).
- Steps:
  - Identify functions with category/question logic (`CurrentCategory`, `AskQuestion`, `InitializeQuestions`).
  - Extract `GetCategoryFor(place)` from `CurrentCategory`.
  - Extract `GetQuestionFor(category)` from `AskQuestion`.
  - Inline the single dependency of `InitializeQuestions`.
  - Use automated refactoring to move these to a new `Questions` class.
  - Move `InitializeQuestions` into the `Questions` constructor.
  - Introduce an array of categories.
  - Update `GetCategoryFor` to use `categories[index % categories.length]`.
  - Introduce a dictionary mapping categories to lists of questions.
  - Update `InitializeQuestions` to fill both structures, then migrate fully.
  - Update `GetQuestionFor` and remove the old structure.
  - Refactor `InitializeQuestions` to use the categories array for initialization.

### Concrete (Participants)
The facilitator can choose the approach:
- For experienced teams: Replicate the refactoring from memory, based on the demo.
- For less experienced teams: Use the detailed step list above as guidance.

### Reflect
Discuss as a group:
- What are the advantages of preparatory refactoring?
- When should you use it?
Participants may jot down thoughts before sharing.
