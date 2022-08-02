---
layout: default
title: Approval Testing Intro
parent: Approval Testing
grand_parent: Workshops
nav_order: 1
---

# Introduction to Approval Testing

This first module goes through the main characteristics of Approval testing:

- Test cases check actual program output against a previously approved value, and any difference will fail the test.
- Normally, a human inspects and approves some actual program output when creating a test case.
- Raw program output may be processed into a more convenient format before being used for approval and comparison.
- Design a Printer to display complex objects, instead of many assertions.
- If actual program output is not yet available, the approved value may be a manual sketch of the expected output.
- Approved values are stored separately from the sourcecode for the test case, although in the same VCS repository.
- When a test case fails, you can use a tool to inspect the differences and easily update the approved value.

We work through some exercises and gain experience with the ['Approvals'](https://github.com/approvals) tool. We will work in small groups and each group can agree which programming language to use. The exercises are generally available in Java, C#, Python and C++.

## Session Outline
 
* 10 min connect: Approval Testing warm up questions 
* 10 min connect: Short introductions and form groups
* 10 min concept: Demo
* 30 min concrete: Do some approval testing
* 5 min conclusions: How about?

_short break_

* 5 min connect: Read through the How about? questions and add more you think of
* 5 min connect: Does fixing the tests take longer than fixing the code?
* 10 min concept: Characteristics of Approval testing
* 10 min concrete: Update some existing tests
* 5 min concept: Approval testing detects both bugs and features
* 20 min concrete: Update tests making one change at a time
* 10 min conclusions: How can you reduce test maintenance?

_short break_

* 2 min connect: is testability an architectural concern?
* 10 min concrete: analyse the problem
* 10 min concrete: Demo pre-comparison processing
* 20 min concrete: fix the problem your own way
* 10 min concept: Pre-comparison processing
* 5 min conclusions: Strategies for testability

_short break_

* 15 min connect: introduce Approvals Puzzles
* 10 min concept: Text-Based testing
* 15 min concrete: Demo Approvals Puzzles
* 5 min conclusions: Strategies for varying output

_short break_

* 5 min concept: Remaining characteristic - sketching
* 15 min concrete: demo of sketching a new test case
* 10 min conclusions: walkabout posters & code review
* 15 min retrospective: gather observations

## Part 1

Use this learning hour ["Approval Testing plain text strings with Verify"](/learning_hours/legacy/approval_testing_intro.html). As well as answering warm up questions, introduce yourselves and form groups of 2-4 where you agree on a programming language. Mix up people from different companies.

### Conclusions - How about?

* On a sticky note, write a question you want answered about Approval Testing
* Stick it on the “How about?” board
* Take a break

## Part 2

Work in small steps. First go through 'how about' questions. Link to them when explaining approval testing characteristics. Follow this learning hour: ["Test Maintenance"](/learning_hours/legacy/test_maintenance.html)


## Part 3

Handling tricky output. Follow this learning hour: ["Design for Approval Testing"](/learning_hours/legacy/handle_dates.html)

## Part 4

More tricky output - filtering and sorting. Follow this learning hour: ["Approvals Puzzles"](/approval_testing_texttest/run_dependent_text.html)

## Part 5

Sketching.

### Concept - Sketching

- If actual program output is not yet available, the approved value may be a manual sketch of the expected output.

### Concrete: demo of sketching a new test case

Add Tax calculations to the receipt. Sketch it first.

### Conclusions: walkabout posters & code review

Get people to look through everything we've done today and discuss with someone what they've learnt. Write answers on the mind-map as sub-nodes.

Nodes on the mindmap:

* When should an Approval Test fail?
* How do you create a new Approval Test?
* Is an Approval Test a kind of unit test?
* Where should you store Approved output?
* Can I combine approvals and assertions in the same test case?
* Can you use Approval testing with all kinds of program output?
* Can you write Approval tests for a program that doesn't exist yet?
* How should you update a program that has Approval tests?
* How should you update Approved output?

### Retrospective: gather observations

Ask people to note down what has happened today in these categories:

* Liked
* Learned
* Lacked
* Longed for


