---
theme: approval_testing_legacy
title: Test maintenance
kata: supermarket_receipt
difficulty: 2
author: emilybache
affiliation: ProAgile
---

# Test maintenance

Work in small steps.

## Session Outline

* 5 min connect: Does fixing the tests take longer than fixing the code?
* 10 min concept: Characteristics of Approval testing
* 10 min concrete: Update some existing tests
* 5 min concept: Approval testing detects both bugs and features
* 20 min concrete: Update tests making one change at a time
* 10 min conclusions: How can you reduce test maintenance?

### Connect: Does fixing the tests take longer than fixing the code?

Have you had this experience that fixing the code takes 5 minutes then you spend days updating the tests? Why does that happen? I would like you to tell me at least 3 reasons.

### Concept - Characteristics of Approval testing

Go through the characteristics of approval testing they should have come accross already. Remind them what an approval test is.

- Test cases check actual program output against a previously approved value, and any difference will fail the test.
- Normally, a human inspects and approves some actual program output when creating a test case.
- Design a Printer to display complex objects, instead of many assertions.
- Approved values are stored separately from the sourcecode for the test case, although in the same VCS repository.

### Concrete - update some existing tests

Practice using the diff tool to inspect differences and approve those that aren't bugs. Use the java, python or C++ version of [Supermarket Receipt](https://github.com/emilybache/SupermarketReceipt-Refactoring-Kata) on the 'with_broken_tests' branch. Note down any bugs you find and any features you find. Approve output and fix bugs as you find them.

### Concept - Approval testing detects both bugs and features

Additional characteristic we have come accross now:

- When a test case fails, you can use a tool to inspect the differences and update the approved value.

Explain what 'over-specified' tests are and why they could be bad.

### Concrete - Update tests making one change at a time

Use the java, python or C++ version of [Supermarket Receipt](https://github.com/emilybache/SupermarketReceipt-Refactoring-Kata) starting on the 'break_tests_incremental' branch. Follow the instructions in the README file to apply changes one by one. After each change, note down if you find a feature or a bug. Approve tests and change code as necessary to approve the output or fix each bug.

Note: this repo [ApprovalTools](https://github.com/emilybache/ApprovalTools) has some useful little scripts such as [approve_all.py](https://raw.githubusercontent.com/emilybache/ApprovalTools/master/approve_all.py) You could usefully put it in your /usr/local/bin.

By the end, your code should look the same as the branch "with_broken_tests". Note observations on sticky notes.

### Conclusions - How can you reduce test maintenance?

Note your ideas on sticky notes. Are any of these strategies only relevant for approval testing? Share with the group.
