---
theme: test_doubles
title: Mocking Dependencies
kata: single_sign_on
difficulty: 4
author: emilybache
affiliation: ProAgile
---

# Mocking Dependencies
Although 'Test Double' is supposed to be the umbrella term for all kinds of mocks, fakes and stubs, in practice people tend to say 'mock'. That's fine in most cases, but it is probably useful to know what the difference is between a mock and other kinds of test double.

### Connect 
On the topic of Test Doubles - give me [three facts]({% link _activities/connect/three_facts.md %}).

### Concept - Mocks
Instead of launching straight into the theory, first get them to review the [SingleSignOn](https://github.com/emilybache/Single-Sign-On-Kata) code and existing test. The test is slow and unreliable. How could you redesign it to make it faster and more reliable?

Hopefully they will realize a test double would help here, and they might suggest replacing the AuthenticationGateway with a stub. That would work, but is a little bit indirect. Another way to do it is to replace the SingleSignOnRegistry with a mock. That makes the test setup a little simpler, and the test faster.

Go through what a mock is and how it is different from a Stub. You could also mention the difference between a Mock and a Spy. 

### Concrete
Have them change the test in [SingleSignOn](https://github.com/emilybache/Single-Sign-On-Kata) to use a mock. In this case a spy helps because it lets us verify a particular call is made - it's really important we ensure the service always validates the token, and actually for this test we don't really want to check the exact response text. That is likely to change often, and will be validated in other tests.


### Conclusions
In your own words, summarize the most important things you want to remember about test doubles. Explain to one another in pairs or write a note to yourself.