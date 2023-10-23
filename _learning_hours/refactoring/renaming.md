---
theme: refactoring
name: renaming
title: Renaming Variables, Fields and Types
kata: Finder
difficulty: 1
author: codecop
---

# Renaming Variables, Fields and Types

[Cryptic names]({% link _code_smells/mysterious_name.md %}) are a common code smell. Renaming them on the spot is often a good strategy in this situation. This learning hour is about renaming.

## Learning Goals

* Recognize importance of (domain specific) names.
* Read by refactoring names.
* See how better names cascade into the old code.

## Session Outline

* 15 min connect: Fill-in-the-blanks "Naming"
* 5 min concept: Importance of domain specific names / demo.
* 35 min concrete practice: Rename the Finder
* 5 min conclusion: Round-robin "What did you learn?"

### Connect - Fill-in-the-blanks "Naming"

Prepare a fill in the blank exercise with at least 10 missing words in several paragraphs about readability and naming. (Chat-GPT works ok for this.) This is a self-correcting exercise. Each participant works on his/her own.

### Concept - Discuss importance of domain specific names

[Lecture]({% link _activities/concept/lecture.md %} ) using slides or frames: Recap the warmup's important things about naming. Only show a summary. Then state the importance of names being from the problem domain. This is one of the most important things about naming.

If necessary do a [short demo]({% link _activities/concept/code_demo.md %} ) of rename in the chosen refactoring tool and show what works and what does not work.

## Concrete Practice - Rename the Finder

The [Finder Refactoring Kata](https://github.com/codecop/Finder-Refactoring-Kata) is small but terrible code. No one can understand what it does. At least there are unit tests to prove the code is working. You job is to refactor the code and make it readable, while keeping the code in working order (pass all tests). (Quoted from its readme)

People [work in pairs]({% link _activities/concrete/work_in_pairs.md %} ). Make sure people start working on the `Finder` class, which is the entry point.

### Facilitation Hints (spoiler)

Do not read ahead before you have tried the kata yourself. Here are some spoiler hints to help people if they are stuck.

* The `Thing` is a person.
* `D` is the date distance between two people.
* `F` is pair of persons.
* The enum `FT` for min and max, sorting for minimal or maximal date distance.

## Conclusions - What did you learn?

Ask "What did you learn about Rename?" and then, when the group size allows, do a [round-robin style answering]({% link _activities/conclusions/collect_round_robin.md %} ) the question. Ask participants to list 3 things each. If the group is larger, let them talk to each other.
