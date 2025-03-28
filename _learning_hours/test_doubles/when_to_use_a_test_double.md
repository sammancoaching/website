---
theme: test_doubles
title: When to use a Test Double
kata: delivery_controller
difficulty: 5
author: emilybache
affiliation: ProAgile
tags: test_doubles test_design
---

# When to use a Test Double
Dependencies of the class under test can be replaced with a test double. Sometimes you don't even need a double at all - you can just use the real collaborator.

### Connect - recap
[Explain these concepts]({% link _activities/connect/explain_previous_concepts.md %}):

* Test Double
* Stub
* Fake
* Mock
* Awkward Dependency
* Dependency Injection

### Concept - When to use a Test Double
Explain when you might want to use a test double - to replace an awkward dependency. Stubs and Fakes are simpler than Mocks and Spies - the latter will fail the test if they are not called correctly.

Point out you don't need to replace a ValueObject with a double. (Could do with an example here!) You might not even need to replace a more complex collaborator with a double. Usually only need a stub if the real collaborator is slow, unreliable or otherwise difficult to use in a unit test. Only need a mock if you need to check the collaborator received correct calls or data.

Perhaps note there are two main schools of TDD - this advice is from the 'classic' or 'Chicago' school. Other TDD practitioners may prefer to use doubles for all collaborators even if they are not slow or unreliable, to isolate the unit under test.

### Concrete
[DeliveryController](https://github.com/emilybache/DeliveryController-Refactoring-Kata) - there are two collaborators - EmailGateway and MapService. Should you replace both with test doubles? What kind of test doubles? Discuss this question first, and agree a strategy. Split into pairs to work on implementing tests.

### Conclusions
In what situations should you use a mock? When would you be better off with an instance of the real object? Note down some answers and share them with the group.
