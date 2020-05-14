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

(short break)

* 5 min connect: Read through the How about? questions and add more you think of
* 10 min concept: Characteristics of Approval testing
* 10 min concrete: Update some existing tests
* 5 min concept: Approval testing detects both bugs and features
* 20 min concrete: Update tests making one change at a time
* 10 min conclusions: explain characteristics to someone else or on sticky notes

(short break)

* 10 min connect: introduce Approvals Puzzles
* 5 min concept: Pre-comparison processing
* 20 min concrete: Do some pre-comparison processing
* 15 min concrete: Demo pre-comparison processing
* 5 min conclusions: Strategies for varying output
* 5 min concept: Text-Based testing
* 10 min concrete: Demo Approvals Puzzles


(short break)

* 5 min concept: Remaining characteristic - sketching
* 15 min concrete: demo of sketching a new test case
* 10 min conclusions: walkabout posters & code review
* 15 min retrospective: gather observations

## Part 1

The general idea.

### Connect - Warm up Questions

Look at these [warm-up questions](../../exercises/warm_up_questions/approval_testing_warm_up_questions.html). Think for yourself then discuss with a pair.

### Connect - Introduce and form groups

Organize people into groups of 2-3 where they can agree on a programming language. Mix up people from different companies.

### Concept - Demo of Approval testing

In the starting position for this exercise, [Supermarket-Receipt-Refactoring-Kata](https://github.com/emilybache/SupermarketReceipt-Refactoring-Kata), there is a test that contains quite a few assert statements to check the contents of the Receipt object. In this demo, add a call to 'verify' from an approval testing library that will replace all these assertions. Use the ReceiptPrinter class to print the receipt to a string that you can verify.

Show that all the information that is checked in individual assert statements are present in the printed receipt. This means that the approval test will catch any errors the assertions would have caught. Note that you can re-use the same printer in many tests, so overall it is not going to be more code. Note that test failures are relatively easy to understand when you use a diff tool.

After the demo - get people to "Think and write" their first impressons

* Think about what you just saw. If you had to explain the main idea to someone else, what would you say?
* Write your explanation in a sentence or two.

### Concrete - Do some approval testing

Have people work in pairs to repeat what you demonstrated, then add further tests for different scenarios. Point out that there are many kinds of discount that should be checked.

### Conclusions - How about?

* On a sticky note, write a question you want answered about Approval Testing
* Stick it on the “How about?” board
* Take a break

## Part 2

Work in small steps.

### Concept - Characteristics of Approval testing

Go through the characteristics they should have come accross already. Answer the questions from the "How about" board if they are relevant here.

- Test cases check actual program output against a previously approved value, and any difference will fail the test.
- Normally, a human inspects and approves some actual program output when creating a test case.
- Design a Printer to display complex objects, instead of many assertions.
- Approved values are stored separately from the sourcecode for the test case, although in the same VCS repository.

Any remaining unanswered questions from the 'How about' board? Either handle them now or say in which module we'll answer them later.

### Concrete - update some existing tests

Practice using the diff tool to inspect differences and approve those that aren't bugs. Use the java version of [Supermarket Receipt](https://github.com/emilybache/SupermarketReceipt-Refactoring-Kata) on the 'with_broken_tests' branch. Note down any bugs you find and any features you find. Approve output and fix bugs as you find them.

### Concept - Approval testing detects both bugs and features

Additional characteristic we have come accross now:

- When a test case fails, you can use a tool to inspect the differences and update the approved value.

Explain what 'over-specified' tests are and why they could be bad.

### Concrete - Update tests making one change at a time

Use the java version of [Supermarket Receipt](https://github.com/emilybache/SupermarketReceipt-Refactoring-Kata) starting on the 'with_tests' branch. Cherry pick each of these hashes in turn. After each cherry pick, note down if you find a feature or a bug in this change. Approve tests and change code as necessary to approve the output or fix each bug.

Note: this repo [ApprovalTools](https://github.com/emilybache/ApprovalTools) has some useful little scripts such as [approve_all.py](https://raw.githubusercontent.com/emilybache/ApprovalTools/master/approve_all.py) You could usefully put it in your /usr/local/bin.

	git cherry-pick 6e73705154fd945875fb836fba03da32a171bd74
	git cherry-pick 46b17c8a7917086ce73b7ff2009f8353c1254ea5
	git cherry-pick 2492b6040cd180e93e2173a4f9414f238ea96310
	git cherry-pick 9e3147930ecd6205979c62ddfeb45c92ba0006b6
	git cherry-pick 5a0f827fccac93c47f3b28d01d297e27452387a5
	git cherry-pick 9c08c046db25194df6ffaece5d21e076b9a62899

By the end, your code should look the same as the branch "with_broken_tests". Note observations on sticky notes.

### Conclusions - explain characteristics to someone else 

In small groups, take turns to explain the characteristics of approval testing. How does it change the way you work? Alternative - write sticky notes

## Part 3

Handling tricky output.

### Connect - Situations where this won't work

In small groups, look through these [Puzzles](https://github.com/emilybache/Approvals-Puzzles). Which ones could you test with approval testing? Which ones would be easier to test a different way?

### Concept - pre-comparison processing

This characteristic: 

- Raw program output may be processed into a more convenient format before being used for approval and comparison.

And to some extent this one:

- Design a Printer to display complex objects, instead of many assertions.


### Concrete - exercise with pre-comparison processing

Use the java version of [Supermarket Receipt](https://github.com/emilybache/SupermarketReceipt-Refactoring-Kata) starting on the 'with_date' branch. All the tests are currently failing. 

* Why are the tests failing?
* Come up with two or three strategies for how to make them pass again.
* Pick a strategy and implement it so the tests pass.

For bonus points, try to use a strategy that fixes the tests but doesn't alter the production code or the ReceiptPrinter or the approved files.

### Demo - pre-comparison processing

Demo solution to the previous exercise. Also demo solutions to these [Puzzles](https://github.com/emilybache/Approvals-Puzzles) using TextTest.

### Conclusions

Review your choices for the [Puzzles](https://github.com/emilybache/Approvals-Puzzles). Do you still make the same choices? Can you think of any more kinds of program output that would not be suitable for Approval testing?

## Part 4

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


