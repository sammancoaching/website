---
title: Bingo Refactoring Kata
kata_name: bingo
---

# Bingo Refactoring Kata

This kata is used for practicing refactoring. The code contains at least the code smells:

- primitive obsession
- data clumps
- missing polymorphism (Board/InitializedBoard/...)
- long methods

The structure of the Bingo Refactoring Kata is similar to the Game of Life kata, but since the focus here is on refactoring, the business rules should be kept as simple as possible. It is not absolutely necessary to understand the business rules in order to complete the task.
The business rules are:

- A bingo board must be initialized before it can be used/played
- A board is initialized when each cell has been assigned a value
- A cell may not be assigned a value that has already been assigned to another cell
- When playing, a cell can be marked as selected

# Refactoring

There are several implementations you can use to practice refactoring in this repo: [Bingo-Refactoring-Kata](https://github.com/sammancoaching/Bingo-Refactoring-Kata).

Various aspects of parallel change can be highlighted:

- Swapping the internal data structure (introducing Cell[][])
- Introducing Coordinate and using it as parameter type. This one would affect the API (method signature) and so we have external dependencies on the “old” API which we should preserve in parallel with the new one. In a real system you’d use Parallel Change to eventually remove the “old” API once all the clients were migrated to the new one.

# Notes

All tests exist twice, one more technically oriented, one more professionally oriented (BDD), please use the one that suits you better.

## Acknowledgement

This kata was first published elsewhere: [Bingo Refactoring Kata](https://github.com/atruvia/samman-coaching-katas/tree/master/bingo-refactoring-kata)
