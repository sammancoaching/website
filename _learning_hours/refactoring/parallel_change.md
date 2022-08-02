---
theme: refactoring
title: Parallel Change
kata: bingo
difficulty: 3
author: pfichtner
via: emilybache
affiliation: Atruvia
---

# Parallel Change

This is a general refactoring strategy for completing a larger change in small steps.

### Connect
[Mark the true statements](/activities/connect/pick_the_correct_items_on_the_list.html) and not the other ones:
1. If you encounter ugly code that you don’t need to change to get your task done, then you don’t need to refactor it.
2. You should get permission from your manager before refactoring.
3. When someone is refactoring the code may be broken for a few days while they do it. 
4. When we invest time in refactoring it saves us time overall.
5. The purpose of refactoring is to make you write code faster.
6. After every four sprints you should do a refactoring sprint.
7. You can only refactor if you have test coverage over 80%.

Ask people in particular about their answers to question 3. Why shouldn't the code be broken for days? What would happen if it was? Have you experienced this? 

### Concept - Parallel Change

One approach to break a refactoring into small safe steps is "parallel change" (also known as expand, migrate, contract). Parallel change could be compared to a road construction site. No one would tear down an existing bridge and redirect traffic through the valley during construction. Normally you would construct the new bridge before the old one is removed. 

In software we have the ability to grow things incrementally. So we can build a new bridge starting with a tiny one where we can divert the pedestrians, then the cars, then the trams and later the trains. It is important here that as soon as we divert the cars to the new bridge, we also remove the road for them from the old one. In this way the new bridge is being built bit by bit while at the same time the old bridge is being dismantled bit by bit but the traffic continues to flow. 

Reference - Danilo Sato has published [an article](https://martinfowler.com/bliki/ParallelChange.html) explaining Parallel Change.

### Concrete: Code Review 
Ask everyone to take a look at this code: [Bingo Refactoring Kata](https://github.com/sammancoaching/Bingo-Refactoring-Kata). What code smells do they see (regardless of whether they can name them or not)? What would be a better structure? 

You are hoping they will spot that there are data clumps and [Primitive Obsession](/code_smells/primitive_obsession.html) - in particular these primitives: 

    String[][] cells 
    boolean[][] marked 

These fields are always written and read in common so there could be a data structure encapsulating both the name attribute (String) and the `marked` attribute (boolean). Refactoring to a `Cell[][]` could be the first step (and this is usually achievable during one learning hour). A further refactoring could be to move a more convenient data structure - instead of `Cell[][]` you could have a Map with `Coordinate` as key and `Cell` as value. 

The group might also suggest some other refactorings - methods that could be broken down to smaller private methods, or replace conditionals with polymorphism (e.g. UninitializedBoard/InitializedBoard/...). Ask them to leave those refactorings for a future learning hour, today we focus on Parallel Change and removing the Primitive Obsession.

### Concrete: Demo
Show them that you are introducing the new structure without removing the old one. Change at least one write access, maybe there is even a read access which you can redirect to the new data structure at this early stage.

### Concrete: Ensemble/Pair Programming
Now, as an exercise, have them start the refactoring again from the beginning and let them do it til the end where the old data structure gets removed.  

If they finish that refactoring quickly, you could ask them to use Parallel Change again to convert the `Cell[][]` to a `Map<Coordinate, Cell>` - an alternate datastructure that removes the primitive obsession on the (x, y) grid co-ordinates.

While the first parallel change focuses on swapping the internal data structure (introducing `Cell[][]`), this next one (introducing Coordinate and using it as parameter type) would affect the API (method signature) and so we have external dependencies on the "old" API which we should preserve in parallel with the new one. In a real system you'd use Parallel Change to eventually remove the "old" API once all the clients were migrated to the new one.

### Conclusions
[Why should you use it](/activities/conclusions/write_important_takeaway.html): What is the most important aspect for you about "parallel change"? 


# Acknowlegements
This learning hour was first published elsewhere: [Parallel Change](https://github.com/atruvia/samman-coaching-website/blob/lh-additions/_learning_hours/refactoring/parallel-change.md)