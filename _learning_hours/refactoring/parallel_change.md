---
theme: refactoring
title: Parallel Change
kata: bingo
difficulty: 3
author: pfichtner
affiliation: Atruvia
---

# Parallel Change

This is a general refactoring strategy for completing a larger change in small steps.

### Connect
[Mark the true statements](/activities/connect/pick_the_correct_items_on_the_list.html) and not the other ones:
1. If you encounter ugly code that you don’t need to change to get your task done, then you don’t need to refactor it.
1. You should get permission from your manager before refactoring.
1. When someone is refactoring the code may be broken for a few days while they do it. 
1. When we invest time in refactoring it saves us time overall.
1. The purpose of refactoring is to make you write code faster.
1. After every four sprints you should do a refactoring sprint.
1. You can only refactor if you have test coverage over 80%.

Ask people in particular about their answers to question 3. Why shouldn't the code be broken for days? What would happen if it was? Have you experienced this? 

### Concept - Refactoring

Refactorings should be approached in small steps. Various patterns can help us with this. It is important that we do not start any major refactoring where we only receive feedback hours or days later as whether the refactoring was successful or not. It makes more sense to proceed in small steps. However, these small steps are only useful if we can also get feedback after each individual step. Automated tests help us with this. We can use them at any time to get feedback on the current state of the refactoring.

One approach is "parallel change" (also known as expand, migrate, contract). Parallel change could be compared to a road construction site. No one would tear down an existing bridge and directing traffic through the valley during construction. Normally everybody would construct the new one before the old one is teared down. 

In software we have the ability to grow things incrementally. So we can build a new bridge starting with a tiny one where we can divert the pedestrians, then the cars, then the trams and later the trains. It is important here that as soon as we divert the cars to the new bridge, we also remove the road for them from the old one. In this way the new bridge is being built bit by bit while at the same time the old bridge is being dismantled bit by bit but the traffic continues to flow. 

### Concrete: Code Review 
Take a look at the code, e.g. [Bingo](https://github.com/atruvia/Bingo-ParallelChange-Kata) (or any existing code with some internal data structure to change, e.g. Game of Life) with them: What code smells do they see (regardless of whether they can name them or not)? What would be a better structure? The major code smells in the bingo kata is that there are a data clumps and [Primitive Obsession](/reference/code_smells/primitive_obsession.html): 

    String[][] cells 
    boolean[][] marked 

They are always written and read in common so there should be a data structure encapsulating the name attribute (String) and the mark attribute (boolean). So refactoring to a ´Cell[][]´ could be the first step (and this can be done perfectly within this learning hour). Futher refactorings could be not to have a ´Cell[][]´ but having a map with Coordinates as keys and Cells as values. Of course this should be done as parallel changes as well. 

Further (minor) code smeels to improve (code smells) are methods that could be broken down to smaller private methods and replace conditionals with polymorphism (e.g. UninitializedBoard/InitializedBoard/...). 

While the first parallel change focuses on swapping the internal data structure (introducing ´Cell[][]´) the next one (introducing Coordinate and using it as parameter type) would affect the API (method signature) and so we have external dependencies on the "old" API which impacts at what point in time we can migrate/contract the "old" API.  

### Concrete: Demo
Show them that you are introducing the new structure without removing the old one. Change at least one write access, maybe there is even a read access which you can redirect to the new data structure at this early stage. 

### Concrete: Ensemble/Pair Programming
Now, as an exercise, have them start the refactoring again from the beginning and let them do it til the end where the old data structure gets removed.  

### Conclusions
[Why should you use it](/activities/conclusions/write_important_takeaway.html) What is the most important aspect for you about "parallel change"? 
