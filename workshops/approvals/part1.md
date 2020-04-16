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
