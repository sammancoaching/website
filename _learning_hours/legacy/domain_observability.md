---
theme: refactoring
title: Domain Oriented Obervability on Reservation Kata
name: domain_oriented_observability
kata: reservation
difficulty: 2
author: pierrickblons
---

# Domain Oriented Obervability

It's useful to have logging and metrics in our code to understand how it's behaving in production. But sometimes those little calls to loggers or metrics class start to spread all across the code base. It's quite common to see methods with more code dedicated to observability than code actually solving the problem.

In this learning hour we will see how to improve the understandability of code that requires observability.

### Learning Goals

### Session Outline

* 10 min connect: Discussion around logging and metrics
* 10 min concept: Introduce domain oriented observability refactoring
* 30 min concrete: Do Reservation Kata in pairs
* 10 min conclusions: Discussion about this technique in your current code base

### Connect: What is observability to you?
Explain why do you use observability in your code? How does it help you in your daily life as a developer? How does it help the team or the organization ?

### Concept: Domain probe
Explain [Domain probe](https://martinfowler.com/articles/domain-oriented-observability.html#DomainProbe) :
* High-level instrumentation API that is oriented around domain semantics.
* Encapsulates low-level instrumentation plumbing required for observability.

### Concrete: Reservation Kata
Experiment in pair the [Reservation Kata refactoring]() to refactor the code by introducing a Domain Probe in the ReservationService.

Optional: You can setup acceptance tests on the logs and metrics before doing the kata

### Conclusions:
Discuss about the technique, do you think it can help in your current code base? 
