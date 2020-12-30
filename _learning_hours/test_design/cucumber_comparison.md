---
theme: test_design
title: Gherkin intro
kata: leap_years
difficulty: 4
---

# Gherkin intro

Gherkin is the name of the formal language you use with a tool like Cucumber or SpecFlow for test automation. It's often used in Behaviour Driven Development for the outer loop tests of Double-Loop TDD.

## Session Outline
 
* 5 min connect: Demo classic Leap Years
* 10 min demo: Leap Years with Cucumber  
* 25 min do: Write a feature file  
* 10 min reflect: Compare Cucumber with ordinary unit testing

### Connect
Show the plain vanilla TDD implementation of Leap Years first. Don't forget the first step, which is writing up the four test cases on the whiteboard. Implementing the whole Kata only takes a few minutes, and they will probably have seen it before in a previous session. Show it to them again so they remember better.

If you think they are up to it, get them to do the Leap Year kata by themselves instead of you demoing it.

### Demo of Gherkin

Do the Leap Years kata (including the implementation) using Gherkin and Cucumber or SpecFlow. Start from the README and say 'this is what we came up with when we talked to the business person about the new function they want us to build'. Translate the requirements into Gherkin.

<pre>

  Feature: Leap Year

  Write a function that returns true or false depending on whether its input integer is a leap year or not.

  Rule: A leap year is divisible by 4
  Scenario: Typical Common Year
    When the user asks whether 2001 is a leap year
    Then it should respond with "false"

  Scenario: Typical Leap Year
    When the user asks whether 1996 is a leap year
    Then it should respond with "true"

  Rule: It's not a leap year if it's divisible by 100
  Scenario: Typical Common Year
    When the user asks whether 1900 is a leap year
    Then it should respond with "false"

  Rule: It is a leap year if it's divisible by 400
  Scenario: Typical Leap Year
    When the user asks whether 2000 is a leap year
    Then it should respond with "true"

</pre>

Since LeapYears is a relatively small problem to solve, probably any other approach than standard TDD looks like overkill. You might want to explain that people should focus on what the approach looks like rather than whether it is appropriate for this problem. You're using a problem they are familiar with so they can focus on something else.

### Do
Have them write a feature file for another kata.

### Reflect
How is the structure of a Cucumber test the same as an ordinary unit test? How is it different? How would using Cucumber affect these properties compared with writing the test in a unit test framework:

- Readability
- Maintainance Costs

Discuss in pairs or in the whole group.


