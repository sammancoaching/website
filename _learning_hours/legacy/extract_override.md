---
theme: legacy
title: Extract and Override
kata: trip_service
difficulty: 2
author: emilybache
---

# Extract and Override

This is a classic dependency breaking technique from Michael Feathers' book "Working Effectively with Legacy Code". In this session we learn how to use it on the classic coding problem "TripService" by Sandro Mancuso. Emily Bache has made a video ["Breaking Legacy Code Dependencies with Extract and Override"](https://www.youtube.com/watch?v=hwr9bVyXkTY) that explains more and shows a demo using Java.

In Legacy Code we can often times find usages of the Singleton pattern or static method calls to infrastructure functionality scattered around the code. This makes it very hard to try to test these kind of methods. Most of the time, it is not easily possible to change the constructor to inject these services or change the method signature without breaking other code. We still would like to get these methods into a test harness.

## Learning Objectives
- Describe when to use a dependency breaking technique
- Use safe steps to get a method under test with "Extract and Override"

## Session Outline

* 5 min connect: Safe Refactorings for Breaking Dependencies
* 5 min concept: What is a Dependency Breaking Technique
* 10 min demo: Extract and Override
* 35 min do: pair on Trip Service
* 5 min reflect: When should you use this

### Connect - Safe Refactorings for Breaking Dependencies
Make a list of names of refactorings, most of which people should have heard of and know roughly what they do. Ask them to vote for which ones they would feel confident doing without having any unit tests. When everyone has voted, summarize what the majority of people think would be ok. Point out it's about risk. Some refactorings are more risky because you might make a mistake. Some are less risky because they are simpler to get right, or because you have good deterministic tools.

Sample list of refactorings to vote on:

- Rename variable
- Extract method
- Introduce Parameter
- Introduce Guard Clause
- Move Method to another class
- Remove Dead Code

### Concept - What is a Dependency Breaking Technique
Use the chapter from Feathers' book as a basis for presenting what this is.

"Dependency-Breaking Techniques... decouple classes well enough to get them under test" 
    -- Michael Feathers, introduction to chapter 25 in "Working Effectively with Legacy Code"

You could mention that there are 24 such techniques listed and today we will look at one of the simplest ones - Extract and Override.

### Concept - Demo
In the [Trip Service Kata]({% link _kata_descriptions/trip_service.md %}), show how to use 'Extract and Override' to make the code testable. It is hard to test the `getTripsByUser` method, because it uses a Singleton `UserSession` and a database call `TripDAO.findTripsByUser`. We cannot easily inject those dependencies without changing the external interface of `TripService`. 

* Write a unit test for `getTripsByUser` when the logged user is null. 
* The new test should assert an exception is thrown.
* Show that this test fails because of the exception thrown by `UserSession` - it can't be used in a unit test.
* Explain that we can use the 'Extract and Override Call' pattern to overcome this problem.
* Extract a method `getLoggedUser`, make it `protected` in `TripService`.
* Create a `TestableTripService` subclass that overrides `getLoggedUser` to return null.
* Use `TestableTripService` instead of `TripService` in the unit test.
* Show that the test now passes.

Note - this demo is shown  between timestamps 1:43 - 5:21 of the [video](https://www.youtube.com/watch?v=hwr9bVyXkTY).

### Concrete Practice - Trip Service Kata
Give them the goal to repeat what you showed in the demo, and continue to use the 'Extract and Override' technique to handle the `TripDAO.findTripsByUser` dependency. They should write unit tests for these three scenarios:

- Logged user is null
- Logged user and given user are not friends
- Logged user and given user are friends

Encourage them to do the first one by hand, and after that they can use an AI tool if they want to. 

If they complete these three tests quickly, ask them to use the same approach to solve another, similar exercise, for example:

- [Attack Calculator Kata](https://github.com/xrecoba/attack-calculator-kata) by Xavi Ametller.
- [Dependency Breaking Katas Excercise C](https://github.com/codecop/dependency-breaking-katas) by Peter Kofler.

### Conclusions - When should you use this
Get people to discuss [when to use]({% link _activities/conclusions/when_to_use_this.md %}) dependency breaking techniques. You could also ask about any drawbacks they see with the "Extract and Override" dependency breaking technique.
