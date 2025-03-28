---
theme: low_level_c
title: Return the patient
kata: grep_with_marketing
difficulty: 7
author: emilybache
affiliation: ProAgile
tags: c refactoring legacy
---

# Return the patient

Part 4 of 4 learning hours on this theme.

### Learning Goals
- use a checklist to return a patient to the main build
- recognize when the patient is successfully returned and the surgery can be deleted
- question whether using the surgery was worth it

## Session Outline

* 5 min connect: what has happened so far
* 10 min concept: steps to move the patient
* 35 min concrete: move the patient
* 5 min conclusions: Was it worth it

### Connect
Look at this list of steps. Re-order it in the order you'd do these steps in. Compare with others in the group and discuss if there are any differences.

- assess whether the test coverage is good enough to allow refactoring and only proceed once it is
- move the patient back into the main build
- introduce a surgery - a folder with its own CMake project
- move the awkward code into the surgery while keeping the main build working by using a #include
- write unit tests for the patient. As you do, add stubs for any dependencies
- delete the surgery folder
- identify a piece of code we want to write unit tests for. It has awkward dependencies.
- for each awkward dependency, refactor the patient to make it easier to stub
- move the unit tests out of the surgery and into the main/test build


### Concept
Steps to move the patient back into production:
- Move patient code into src/ folder
- Move test cases and stubs to production code tests (test folder)
- Surgery is empty - Delete it

### Concrete
In the exercise repo [Grep with Marketing](https://github.com/objarni/grep-with-marketing) there is a branch 'with_abstractions'. Beginning from there, follow the steps above to move the patient out of the surgery.

### Conclusions
Was using the surgery worth it? Make a list of advantages and disadvantages of the approach we have learnt about over these four learning hours.

