---
theme: approval_testing_legacy
title: Using coverage when adding tests to existing code
kata: product_export
difficulty: 1
---

# Using coverage when adding tests to existing code

Many teams use coverage metrics to assess how good their tests are. In this session we'll use coverage interactively during test development, to help us to add tests to existing code. The warm-up questions might raise a wider discussion about good use of coverage data in the organization, which could be a good thing, but possibly something to defer for a later occasion.

## Session Outline

* 10 min connect: discuss warm-up questions  
* 5 min demo: add test to cover a function
* 35 min do: pair on Product Export Refactoring Kata  
* 5 min reflect: review warm-up questions

### Connect
What do you already know about code coverage? I have some [warm-up questions](https://emilybache.github.io/exercises/warm_up_questions/coverage_warm_up_questions.html) which could be a good way to get you thinking. Have people read and answer the questions for themselves, then discuss in small groups whether they all answered the same.

### Demo Product Export Refactoring Kata
Explain the starting position for [Product Export Refactoring Kata](https://github.com/emilybache/Product-Export-Refactoring-Kata). You want to add tests for ``XMLExporter`` until you have 100% coverage. The starting code contains an empty test that doesn't do anything, but very helpfully, there is some test data available in ``SampleModelObjects``. Write a test case for the first function in ``XMLExporter``, I suggest using Approvals and VerifyXML in particular. Show the coverage. It should be much improved for that function, but not 100%. Leave that for them to fix.

Many IDEs have coverage metrics built in and mark lines of code as covered or not covered in the editor. Before this session make sure you know what tools the team has available to them and take the chance to show them how to use them. For example colour-blind people may need to adjust the IDE settings. 

If you think the group is ready for it and you have enough time, enable branch coverage and explain how it differs from statement coverage.

### Do: Add tests to get 100% coverage
Have people work in pairs to do the exercise. Help them to set up their IDEs as necessary.

The last function they try to write tests for has a twist. The output varies with every run since it prints today's date. Some pairs will be able to work out a way to handle it, others will ask for help. You probably won't have time to help them fix that in this session, assure them you will tackle it in a later session. Ask them to focus on getting 100% coverage for the other functions for the time being.

### Reflect
Give people a chance to review their answers to the warm-up questions. In particular draw their attention to any questions that concern adding tests to existing code, which was today's topic.
