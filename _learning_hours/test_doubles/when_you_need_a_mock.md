---
theme: test_doubles
title: When you need a mock
kata: auction
difficulty: 3
author: emilybache
---

# When you need a mock

In this exercise you need to use a mock or spy to test the code.

There is a video on Emily Bache's YouTube channel that goes through this learning hour ["Mock objects: the Police Enforcer of Unit Testing"](https://youtu.be/4bCuxMhtf_E).

## Session Outline

* 10 min connect: How can you test this?
* 5 min concept: Explanation of test doubles
* 30 mins concrete: Write a test using a test double
* 5 min conclusion: Do you like your design?

### Connect: How can you test this?

Today's exercise is [Auction Test Design Kata](https://github.com/emilybache/Auction-TestDesign-Kata). Review the code in
"AuctionMessageTranslator". It is supposed to parse text messages it receives from an external source, and notify a listener. The messages are about the progress of an online auction.

There are bugs, marked with comments. The listener interface is under development. This listener wants to know what is happening in the auction so it can decide whether to make a bid.

How could you write tests that would fail because of each bug? Discuss in pairs. Don't write any code at this point, just talk.

### Concept: Test Doubles

Explain what a test double is and how we could use one in this problem. You could explain the various different kinds of test double including spy and mock.

### Concrete: Write a test using a test double

Ask people to write tests for each of the bugs using a mock. Each test should fail because of a bug, and pass if you change the code to fix the bug. Through this work you should design the methods in the "AuctionEventListener" interface. 

When you have fixed the bugs, add support for the additional message outlined in the README file in the repo.

### Conclusions: Do you like your design?

Compare the designs you have come up with for the AuctionEventListener interface. Why did we use a test double to develop this code? Ask [When should you use this]({% link _activities/conclusions/when_to_use_this.md %})?
