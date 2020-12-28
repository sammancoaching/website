---
layout: default
title: Using coverage to inform test creation
parent: Approval Testing Legacy Code
grand_parent: Learning Hours
nav_order: 4
---

# Using coverage to inform test creation

The code to test has static methods and readily available test data, which makes it straightforward to get under test.


## Session Outline

* 2 min connect: Approval Testing Characteristics Stand-Up 
* 5 min concept: Legacy code and coverage
* 10 min demo: Coverage in IDE and add tests
* 30 min concrete: Add tests using coverage
* 5 min conclusions: Describe an algorithm for adding tests to existing code

### Connect: Approval Testing Characteristics Stand-Up 

Read out some statements. People stand up if they agree they are true. (Or give thumbs up)

### Concept: Legacy code and coverage

Slides - what is legacy code, how to test it.  Also: get them to configure their IDEs.

### Demo: Coverage in IDE and add tests

Explain the starting position for [Product Export Refactoring Kata](https://github.com/emilybache/Product-Export-Refactoring-Kata). You want to add tests for ``XMLExporter`` until you have 100% coverage. The starting code contains an empty test that doesn't do anything, but very helpfully, there is some test data available in ``SampleModelObjects``. Write a test case for the first function in ``XMLExporter``, I suggest using Approvals and VerifyXML in particular. Show the coverage. It should be much improved for that function, but not 100%. Leave that for them to fix.

Many IDEs have coverage metrics built in and mark lines of code as covered or not covered in the editor. Before this session make sure you know what tools the team has available to them and take the chance to show them how to use them. For example colour-blind people may need to adjust the IDE settings. 

### Concrete: Add tests using coverage

Have people work in pairs to do the exercise. Help them to set up their IDEs as necessary.

The last function they try to write tests for has a twist. The output varies with every run since it prints today's date. Some pairs will be able to work out a way to handle it, others will ask for help. You probably won't have time to help them fix that in this session, assure them you will tackle it in a later session. Ask them to focus on getting 100% coverage for the other functions for the time being.

### Conclusions: Describe an algorithm 

Is what we've done sufficiently mechanical that you could describe an algorithm for adding tests to existing code?
