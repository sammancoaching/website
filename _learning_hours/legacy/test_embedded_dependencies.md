---
theme: legacy
name: test_embedded_dependencies
title: Testing Methods with Embedded Dependencies
kata: trip_service
difficulty: 2
author: mhc03
via: emilybache
---

# Testing Methods with Embedded Dependencies

In Legacy Code we can oftentimes find usages of the Singleton pattern or static method calls to infrastructure functionality 
scattered around the code. This makes it very hard to try to test these kind of methods. Most of the time, it is not easily 
possible to change the constructor to inject these services or change the method signature without breaking other code. 
We still would like to get these methods into a test harness to incrementally break these dependencies and use other refactoring 
methods effectively. Here, we will look into the 'Extract and Override Call' pattern described by Michael Feathers to get 
our Legacy Code under test by practicing it on the [Trip Service Kata](https://github.com/sandromancuso/trip-service-kata).

## Learning Goals

* Recognize why methods similar to shown in the kata are hard to test
* Apply the 'Extract and Override Call' pattern to build a test harness

## Session Outline

* 5-10 min connect: What design pattern is used in the code?
* 5 min concept: Demonstrate the 'Extract and Override Call' pattern.
* 30 min concrete practice: Test and refactor the Trip Service Kata
* 5-10 min conclusion: When should you use this pattern?

### Connect - What design pattern is used in the code?
Open the Trip Service Kata and show the line where the Singleton Pattern is used in the TripService class. Ask, which 
pattern this is and discuss the pros and cons of using this pattern. You could get more specific and ask why it makes 
it hard to test the `getTripsByUser` method it is used in.

### Concept - 'Extract and Override Call'
Show the TripService class and explain that it is hard to test the `getTripsByUser` method, because it uses a Singleton
and a static method call, which ultimately may represent an infrastructure call. We would normally mock these kind of dependencies to have
a quicker and more focused test without relying on real databases or APIs. We cannot inject those dependencies and do not want 
to change the external interface of TripService, neither the constructor nor the method signature, to safely get our class under test.
Changing the external interface in legacy code may result in other code breaking without us realising.

After that explanation, show how to get this class under test by demonstrating the 'Extract and Override Call' pattern.
Depending on the used programming language, there may be some intricacies or specialties you could point out.

## Concrete Practice - Trip Service Kata
Do the Trip Service Kata in an ensemble and apply above theory. Keep track that they first write tests before trying to 
apply the pattern and that they should only extend the `TestableTripService` pattern class after having written the 
appropriate tests for it.

Caveats: When creating the testable subclass of TripService, there may come a moment, where someone suggests to inject mocked
dependencies to the TestableTripService class, instead of injecting the user, which should be returned. In this case, you can 
either let them experiment and choose, which way they prefer or, depending on the time, tell them the way you would approach this.
Generally, you would inject the return values instead of injecting mocks.

If the team is rather quick or already knows this pattern, you can split them into pairs to train this pattern with 
other Katas. These are some Katas which could be used as training:

- [Attack Calculator Kata](https://github.com/xrecoba/attack-calculator-kata)
- [Dependency Breaking Katas Excercise C](https://github.com/codecop/dependency-breaking-katas)

## Conclusions - When should you use this pattern?
Discuss following question with the team: When should you use this pattern? You may even go deeper and outline the main 
idea behind this pattern.

# Acknowledgements
The [Trip Service Kata](https://github.com/sandromancuso/trip-service-kata) is from Sandro Mancuso. He even has a [video](https://www.youtube.com/watch?v=_NnElPO5BU0), 
where he incrementally does the refactoring while explaining all the steps. I would highly recommend trying it first and 
then watching his video. I found this exercise on Nicolas Carlo's [understandinglegacycode](https://understandlegacycode.com/blog/5-coding-exercises-to-practice-refactoring-legacy-code/#3-the-trip-service) 
and a [blog post](https://understandlegacycode.com/blog/efficiently-practice-refactoring-katas/) for the Trip Service Kata specifically. 

The [Attack Calculator Kata](https://github.com/xrecoba/attack-calculator-kata) was provided by Xavi Ametller.

The [Dependency Breaking Katas Excercise C](https://github.com/codecop/dependency-breaking-katas) was provided by Peter Kofler.

Credit belongs to all of them.

