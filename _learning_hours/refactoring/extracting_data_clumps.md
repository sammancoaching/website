---
theme: refactoring
name: extracting_data_clumps
title: Extracting Data Clumps
kata: Hero Quest
difficulty: 2
author: codecop
tags:  refactoring c
---

# Extracting Data Clumps

In legacy code we often lack abstractions. How do we find these missing abstractions? Following code smells gives some ideas.

## Learning Goals

* Recognize code smells Data Clump and Long Parameter List.
* Perform extract C-style struct, record or (data) class in a safe way.
* Find a name for the new abstraction.

## Session Outline

* 5 min Connect: Sort concepts according its relation to abstraction
* 20 min Concept: Explain code smells and how to refactor them
* 30 min Concrete practice: Identify Data Clumps, extract them, name them
* 5 min Conclusion: Discuss Open Question

## Connect - Why do we group related data (and logic together)?

[Sort the following concepts]({% link _activities/connect/sort_these_items.md %} ) according its relation to abstraction (i.e. grouping of related data and logic). There are four in each row, sort by highest relevancy.

* grouping is related to abstraction
  * Modularity (reason: structure a system)
  * Encapsulation (reason: information hiding)
  * Reusability (reason: because in one piece)
  * Maintainability (reason: easier to locate and understand)
* not related
  * Scalability
  * Performance
  * Concurrency
  * Usability

## Concept - Data Clump and Long Parameter List

[Lecture]({% link _activities/concept/lecture.md %} ) using slides or frames about how we could find these missing abstractions? One way is to follow up on some code smells. Explain the code smells and show sample code.

[Data Clump]({% link _code_smells/data_clumps.md %})

* Different parts of the code contain identical groups of variables.
* These clumps should be turned into their own classes.

[Long Parameter List]({% link _code_smells/long_parameter_list.md %})

* More than three or four parameters for a method.

### Scan code for these code smells

[Code Review]({% link _activities/connect/code_review.md %} ): As first exercise, check out the code and look for Data Clumps and Long Parameter Lists. Allow people 5 minutes looking at the code. Then collect the group and ask what they found.

### Demo

Do a 5 minute [demo]({% link _activities/concept/code_demo.md %} ) how to make a struct (recording or slides). Using an example of a student data clump the following steps are necessary:

* There is a data clump of a Student declared and used in a method.
* Define a struct to represent a Student.
* Create an instance of the Student struct with same values.
* Add the Student struct to the method signature and pass the instance (parallel change).
* Use the Student struct in the method's body (parallel change).
* Remove the data clamp from the method signature, now use the struct to pass Student information alone.
* Remove the declared data clump of the Student data.

## Concrete Practice - Hero Quest

The [Hero Quest Refactoring Kata](https://github.com/codecop/Hero-Quest-Refactoring-Kata) contains some pieces of code from a RPG dealing with players and items. People [work in pairs]({% link _activities/concrete/work_in_pairs.md %} ) and follow the code smells to extract data clumps.

### Facilitation Hints

In half an hour people can do one to two iterations, i.e. converting one to two data clumps and using them in one method each.

## Conclusions - Summarise Usage

Ask the group what indications for missing abstraction could there be? How do you recognise these, when you need to introduce an abstraction?

Expected answers are

* Data Clump code smell
* Long Parameter List code smell

Other correct answers include

* Shared prefixes in names
* Struct too big
