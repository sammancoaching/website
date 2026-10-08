---
theme: agentic_engineering
name: show_dont_tell
title: Show, Don't Tell
difficulty: 2
author: mostalive
via: emilybache
tags: agentic feedback prompting
---

# {{ page.title}}

[As Linus Torvalds once put it](https://lkml.org/lkml/2000/8/25/132):  "Talk is cheap. Show me the code". With agentic engineering creating code has become rather cheap, but the agent doesn't always understand what code you want - so it can still be a better idea to "Show me the code". In this learning hour we go through a pattern for this kind of agentic prompting - "Show, Don't tell". This pattern is fairly similar to the [Show the agent, let it repeat](https://ai-coding-patterns.dev/patterns/show-the-agent-let-it-repeat-automate/) augmented coding pattern, except we use the commit history as a reference instead of markdown.

## Learning Goals

* Use a concrete code example (show, don't tell) to guide a coding agent in propagating a pattern across a codebase.
* Produce your own example, then show the result to the agent as the pattern to follow.
* Identify when to use this agentic prompting technique - when it's more accurate to explain what you want with a code example than with words.

## Prerequisites
The learners should already be able to spot unit test smells such as a poorly written assertion and/or too many 'Act' steps.

## Session Outline

* 5 min connect: What do you do when the agent doesn't write the code you want it to? 
* 10 min concept: Show Don't Tell
* 10 min concept: Demo - improve assertion
* 10 min concrete: Follow the example in the previous commit
* 15 min concrete: Create an example to follow
* 5 min conclusions: When should you use this

### Connect
Ask - "What do you do when the agent doesn't write the code you want it to?" You are hoping they will talk about various strategies, including giving it an example. 

This is an [Open Question]({% link _activities/connect/open_question.md %}) connect.

### Concept
Ideally tell a story from your experience about a time when you used this prompting pattern. An example where your agent failed when you told it what to do in words, but then succeeded when you used this pattern: 

* make one example of what you want (possibly by hand-coding)
* Make a commit (or short series of commits) with only that change
* Ask it to look at the example and find other, similar places in the code
* Ask it to apply this change in only those other places

You can let your coding agent dig through its' history to find examples where you applied this, and help you make a couple of slides illustrating the steps.

If you don't have a concrete code example you can talk about, explain the pattern in general terms.

### Demo
The exercise repo [Show Don't tell](https://github.com/sammancoaching/show-dont-tell) contains two exercises and a suitable demo. For the demo, use `OrderCompletionTests`. The assertions in this class treat the Order as a kind of data record where you check the values of individual fields. This makes the tests hard to read and understand. You want to be able to treat the Order like a domain object, asserting things like 'IsFullyPaid'.


* In the first test, replace the existing assertions with a check that `order.IsFullyPaid` is True. 
* Commit that change. 
* Prompt the agent using the "show don't tell" pattern to update the other tests in this class.

### Concrete Practice 1 - Use an existing example
The first exercise is to improve the test cases in "OrderTotalTest". The first test is already improved, and you need to use the "show don't tell" pattern to update the rest.

Sample prompt:

    We used a custom matcher in DiscountOnFirstLine_TotalAndLineValues
    Are there other tests in the same file that can use this matcher?

That prompt might need adjusting for the specific test name in the language you are using.

The outcome you are hoping for is that the AI tool will update all the tests in that file with the same pattern.

### Concrete Practice 2 - Create an example, apply it appropriately
The second exercise is to improve the tests cases in "OrderBookLifeCycleTest". Identify and name the design problems in the first test, fix them, then use the "show don't tell" pattern to update other similar test design problems in this class.

Exercise instructions:
* Improve the design of the first test case by splitting it into two test cases
* Commit with a good message
* Ask the coding agent to look at the previous commit and identify other places you could do the same design improvement.
* Ask the coding agent to update the other appropriate test cases.

The outcome you are hoping for is that the AI tool will update all the tests in that file that have the same design problem, and not the others.

### Conclusions
Ask "When should you use this - and when would this approach fail?" Hopefully people will explain that it works best when  agents would otherwise misinterpret an instruction given in words. This approach can still fail if the agent identifies the wrong places to apply the example pattern.

This is a [When should you use this]({% link _activities/conclusions/when_to_use_this.md %}) activity. 
