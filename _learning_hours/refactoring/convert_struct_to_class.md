---
theme: refactoring
name: convert_struct_to_class
title: From Struct to Class
kata: Hero Quest
difficulty: 2
author: codecop
tags:  refactoring c
---

# From Struct to Class

After extracting [Data Clumps to (C style) structs]({% link _learning_hours/refactoring/extracting_data_clumps.md %} ), we want to go further and make real classes.

## Learning Goals

* Know the benefits of grouping into classes.
* Perform conversion of C-style struct, record or (data) class to real (C++ style) class in a safe way.
* Encapsulate the data of the new abstraction.

## Session Outline

* 5 min Connect: Web Hunt on Information Hiding
* 10 min Concept: Demo Converting Struct to Class
* 35 min Concrete practice: Hero Quest (with structs)
* 5 min Conclusion: Summarise Benefits

## Connect - Web Hunt on Information Hiding

[Web Hunt]({% link _activities/connect/webhunt.md %} ) on the following question: What is Information Hiding? What is Encapsulation? Why do we want them?

* Let participants search the web and collect key concepts.
* For example, start with Wikipedia, https://en.wikipedia.org/wiki/Information_hiding

The following things could come up:

* hides complexity
* eases re-usability
* increases readability
* helps with testing
* protect internal stuff
* etc.

Besides the connect part, this helps you to assess if participants know the theory.

## Concept - Converting Struct to Class

Start with [Lecture]({% link _activities/concept/lecture.md %} ) of two slides to summarise both concepts:

Information Hiding:

* Means restricting direct access to some of the module's components.
* Usually hides implementation details like data structure or algorithm used.

Encapsulation:

* Is (usually) an object oriented term.
* Objects are defined by what they do, not what they contain.
* All data should be hidden within its class.

### Demo

Do a 5 minute [demo]({% link _activities/concept/code_demo.md %} ) how to convert a struct to a class (recording or slides). Using an example of a student struct the following steps are necessary:

* There is a struct of a Student declared and used in some methods.
* Convert the struct to a class. And remove "struct" in all signatures.
* Create a public constructor for initialisation.
* Use the constructor for initialisation.
* Copy methods working on the class into the class (parallel change).
* Replace the main parameter with the *this* pointer.
* Call the instance method instead of stand alone one (parallel change).
* Remove stand alone method(s).
* Make fields private to encapsulate them.
* Rename methods accordingly the new context.

## Concrete Practice - Hero Quest

The [Hero Quest Refactoring Kata](https://github.com/codecop/Hero-Quest-Refactoring-Kata) contains some pieces of code from a RPG dealing with players and items. Either continue after the previous learning hour or use the branch *with_struct*, where the structs have been created. People [work in pairs]({% link _activities/concrete/work_in_pairs.md %} ) and follow the steps to convert the existing structs to classes in a safe way. They also need to encapsulate their data.

### Facilitation Hints

In half an hour people can do one iteration, i.e. convert one class and moving one or two methods into it.

## Conclusions - Summarise Benefits

Ask the group to summarise the benefits of grouping data and methods together. Also ask for encapsulation.
