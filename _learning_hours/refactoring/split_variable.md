---
theme: refactoring
title: Split Variable
name: split_variable
code_smell: variable_with_long_scope
kata: tennis
difficulty: 3
author: emilybache
---

# Split Variable

Practice this refactoring.

There is a video on Emily Bache's YouTube channel for this learning hour ["Prepare a Code Paragraph for Extraction with Split Variable"](https://youtu.be/wPmJz2ynb3k)

## Session Outline

* 5 min connect: Identify Paragraphs
* 5 min concept: Split Variable
* 10 min demo: show the patterns and the shape of the refactoring
* 25 min concrete: practice Split Variable
* 5 min conclusions: note down learnings

## Connect: Identify Paragraphs
If the group is not familiar with code paragraphs then you should do a learning hour on that before this one. The purpose of this connect exercise is to remind them what they already know about code paragraphs by having them review some code and identify paragraphs.

For example, show them [Theatrical Players](https://github.com/emilybache/Theatrical-Players-Refactoring-Kata). 

## Concept: Split Variable Refactoring
The reason to do split variable is often so that you can more easily extract a method for a code paragraph. Refer to [Split Variable]({% link _refactorings/split_variable.md %}) for a description of this refactoring. There are several code katas I commonly use that use it. It's a small refactoring move that's hard to practice in isolation so I usually show it several times in these different situations.

## Demo: show the patterns and the shape of the refactoring
Depending on how confident your group will be able to do these refactorings, you may or may not need to show all of these as demos.

1. **Plain re-use**. In Tennis 3 there is a variable 's' that is re-used both as a score name and a player name. The variable is re-used so you need to redeclare it for each new use.

2. **Accumulating variable** In Tennis 7 there is a variable 'result' that is appended to throughout the long method 'getScore'. Before you can extract methods for each part, it is convenient to split the 'score' variable into for example 'tieScore' and 'regularScore'. This kind of accumulating variable can also be an integer like the 'volumeCredits' in Theatrical Players.

3. **Calculated Datamember** In Office Cleaner 9 there is a method 'parseInput' that calculates two datamembers - coordHashSet and position. If you want to extract parts of this calculation to a testable pure function then it will need to be passed the current state of these datamembers explicitly. You split the assignment of the datamember from the calculation of its value by introducing a new variable for the calculation, then assigning it at the end.

## Concrete: do split variable
Set the group loose on the refactoring in all the examples you've shown. Make sure they have access to the [list of the safe steps]({% link _refactorings/split_variable.md %}) for all variants of this refactoring, and remind them to use their tools.

## Conclusions: when will you use this?
How will you notice you need 'split variable'?  What will you do then? This is a [Write important takeaway]({% link _activities/conclusions/write_important_takeaway.md %}) conclusion.

