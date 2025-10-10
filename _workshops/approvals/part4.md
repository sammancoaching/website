---
layout: default
title: Approval Testing with Microservices
parent: Approval Testing
grand_parent: Workshops
nav_order: 4
---

# Approval Testing with Microservices

Microservices is a popular architectural choice today, and it opens up new possibilities for automated testing. We will look at how you could use Approval testing to:

- test one microservice via its api
- test a group of microservices fulfilling a whole user-perspective scenario

We will work in small groups to write tests for an example microservice application. 


## Session Outline

* 10 min Connect: What are the characteristics of a microservice architecture?
* 10 min Concept: my experiences of testing Microservices
* 15 min Concrete: explore Restful Booker
* 10 min Concrete: write down checks we could do
* 10 min Concrete: write down risks & match with checks
* 5 min Conclusions: How does microservice architecture affect test strategy?

_short break_

* 5 min Connect: How can you use approval testing with this microservice?
* 10 min Concept: test fixture demo
* 30 min Concrete: Write tests/checks and note down bugs
* 5 min Demo: show sample solution
* 5 min Conclusions: Would this work in other situations?

_short break_

* Connect: Your experiences testing microservices
* Concept: Empowered teams and test strategy
* Concrete: End-to-end functional test example
* Conclusions: What is simpler what is harder with approvals

_short break_

* Connect: Who to ask when a test fails?
* Concept: Tracing for debugging
* Concrete: Examine example traces to find buggy service
* Conclusions: Distributed tracing in an approval test?


## Connect: What are the characteristics of a microservice architecture?

Write sticky notes individually. 1-2-4-all

## Concept: microservices test strategy

Change in test strategy compared with a monolithic architecture. Use the additional APIs that you have. Less 'whole system' thinking. Test one microservice by itself.

## Concrete: Explore 'restful booker'

Scenario: You work on a product for hotel bookings. Right now have only a few hotels using it, one instance per hotel. Come to the point we need some automated tests for it. Imagine this service is part of a larger system with other services for hotels.

* explore what the application does
* find the documentation

We're using [my fork](https://github.com/emilybache/restful-booker) of Mark Winteringham's code.

## Concrete: write down Checks we could do

A Test is when I'm hoping to discover something I don't know. A Check is when I already know something, and the check will tell me if anything has changed. Write a list of checks you could do on this code. 1-2-4-all.

## Concrete: risks

What could go wrong with this microservice? What could cause it to stop being available and useful? What could work badly and cause problems for users? 1-2-4-all

Match the risk list with the checks list from earlier. Can we think of additional checks now? Can we prioritize our checks?

## Conclusions: How does microservice architecture affect test strategy?

Note the process we used now to come up with a test strategy for this microservice. Is anything different about it compared with any other kind of application or architecture?

_short break_

## 5 min Connect: How can you use approval testing with this microservice?

Based on what you already know about approval tests, how would you apply an approval testing approach to this microservice? Discuss in pairs, report findings to group.

## 10 min Concept: test fixture demo

What it does, how to use it.

## 30 min Concrete: Write tests/checks and note down bugs

Add test cases for rest api endpoints. Use the prioritized check list you made earlier.

## 5 min Demo: show sample solution

My best efforts are in the 'with_tests' branch

## 5 min Conclusions: Would this work in other situations?

If you had a different microservice in a different application, what have you learnt today that you could apply to it?


_short break_

## Connect: Your experiences testing microservices

Have you ever worked with a microservices architecture? Did you have any end-to-end tests?

## Concept: Empowered teams and test strategy

slides about my experiences and Accelerate research

## Concrete: End-to-end functional test example

Using [BeeFriendly](https://github.com/emilybache/BeeFriendly). Examine the existing test and write another one. 

## Conclusions: What is simpler what is harder with approvals

Particularly looking at the use_case.py file. How does this compare with other selenium tests you've seen and worked with?

_short break_

## Connect: Who to ask when a test fails?

Has this ever been a problem for you?

## Concept: Tracing for debugging

Slides about my own experiences

## Concrete: Examine example traces to find buggy service

Using [BeeFriendly](https://github.com/emilybache/BeeFriendly). Register for a newsletter and examine the trace with jaeger. Which service is buggy?

## Conclusions: Distributed tracing in an approval test?

What do you think about using distributed tracing as part of the approval test?

## Session conclusions

Mind map questions
- What kinds of test would you normally include in a microservices test strategy?
- what is an empowered team?
- What is distributed tracing for?
- Are there any risks specific to microservices applications that testing should address?
- How does it change a selenium test case if you use approvals to verify the html?
- What printers do you need in a microservices architecture?


