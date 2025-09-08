---
theme: legacy
title: Extract and Override
kata: trip_service
difficulty: 2
author: emilybache
---

# Extract and Override

"Extract and Override" is a classic dependency breaking technique from Michael Feathers' book "Working Effectively with Legacy Code". In this session we demonstrate it using the classic coding problem "TripService" by Sandro Mancuso.

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
Show the [Trip Service Kata](https://github.com/sandromancuso/trip-service-kata) and how to use 'Extract and Override' to make the code testable. Do a more or less detailed demo depending on how much your audience needs to see before trying it themselves.

### Concrete Practice - Trip Service Kata
Give them the goal to test three scenarios for this method:
- Logged user is null
- Logged user and given user are not friends
- Logged user and given user are friends

Ask them to use the 'Extract and Override' technique to achieve that.

### Conclusions - When should you use this
Get people to discuss [when to use]({% link _activities/conclusions/when_to_use_this.md %}) dependency breaking techniques. You could also ask about any drawbacks they see with this particular dependency breaking technique "Extract and Override".
