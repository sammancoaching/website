---
theme: test_design
title: Stubbing Dependencies
kata: tire_pressure
difficulty: 3
author: emilybache
affiliation: ProAgile
---

# Stubbing Dependencies
Dependencies of the class under test can be stubbed. Sometimes you don't even need a stub at all - you can just use the real collaborator.

### Connect - three facts and a question
On the topic of Stubs - give me [three facts](/activities/connect/three_facts.html).

### Concept - When to Stub
Explain when you might want to use a stub - to replace an awkward dependency. Stubs are simpler than Mocks: they won't fail the test if they are not called. 

Demo creating a stub with their preferred mocking framework. Point out you don't need to replace a ValueObject with a stub. You might not even need to replace a more complex collaborator with a stub. Usually only need a stub if the real collaborator is slow, unreliable or otherwise difficult to use in a unit test.

Perhaps note there are two main schools of TDD - this advice is from the 'classic' or 'Chicago' school. Other TDD practitioners may prefer to use stubs for all collaborators even if they are not slow or unreliable.

### Concrete 
[DeliveryController](https://github.com/emilybache/DeliveryController-Refactoring-Kata) - there are two collaborators - EmailGateway and MapService. Should you replace both with test doubles? What kind of test doubles? Discuss this question first, and agree a strategy. Split into pairs to work on implementing tests.

### Conclusions
In what situations should you use a stub? Note down some answers and share them with the group.

