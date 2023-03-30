---
theme: approval_testing_texttest
title: Sandboxing Introduction
kata: calc_stats
difficulty: 2
author: emilybache
affiliation: Bache Consulting
languages: c,texttest
---

# Sandboxing Introduction
Sometimes you need to adapt your application a little bit to make it testable. In this learning hour we find out how to sandbox an application that needs a physical keyboard press before it will do anything.

## Learning Objective
* Explain what sandboxing is and why you'd want to do that

## Outline

* 5 min connect: Characteristics of a good test
* 15 min concept: What is sandboxing
* 30 min concrete: Write tests for CalcStats
* 5 min conclusions: When should you use this?

## Connect - Characteristics of a good test
Give me [three characteristics]({% link _activities/connect/three_facts.md %}) of a good test case that you'd like to have.

Hopefully someone will mention 'not flaky' or 'repeatable'. If not, suggest it.

## Concept - Sandboxing
Begin by a demo of the program we're going to test today - [CalcStats](https://github.com/emilybache/CalcStats-TestDesign-Kata), specifically the "c_texttest" version of it. Show how to run the program on the command line and that it requires input from the keyboard. Show how the code mixes together the logic that gets user input and displays results with the calculation logic. This is going to be awkward to test automatically, and you'd really like to have some tests in place before you refactor to separate the logic from the I/O code.

Explain the idea of 'Sandboxing' and how we want to make the minimum possible change to make the code testable. Ask them what the CalcStats program tries to access that is outside of the sandbox. Hopefully they will notice that it needs some input files, and also a keyboard press.

Demo how to modify the code so that it uses kbhit_wrapper and getchar_wrapper to prevent it needing a keyboard hit. Show how to supply files and standard input with TextTest.

## Concrete - Write tests for CalcStats
Hand over to them to write tests using TextTest. Ask them to cover the main functionality for the various kinds of statistics. If they finish that quickly, you can also ask them to refactor the code to make it possible to unit test each calculation function separately.

## Conclusions - When should you use this?
You're hoping they will notice how small a code change they needed to make this testable, and then how quickly they were able to create good tests. Facilitate a discussion and prompt them all to reflect on [when you can do this]({% link _activities/conclusions/when_to_use_this.md %}), what problems sandboxing solves, and what problems remain.



