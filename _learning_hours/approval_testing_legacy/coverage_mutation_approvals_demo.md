---
theme: approval_testing_legacy
title: Demo of Approvals with Coverage and Mutation testing
kata: gilded_rose
difficulty: 3
---

# Gilded Rose Demo

This is some really horrible legacy code, and it is so satisfying to refactor it! This exercise is the most popular one I have, judged by the number of stars and forks and pull requests I get for it. In this learning hour you show a full worked solution, demonstrating several techniques. The idea is that attendees will come away with a bigger picture of what's possible to achieve, and higher ambitions for their own work with legacy code.

## Session Outline
 
* 5 min connect: how to refactor code you don't understand?  
* 45 min demo: Gilded Rose worked solution
* 5 min reflect: Techniques to read up on

### Connect
In pairs, spend a couple of minutes identifying strategies you would use when presented with code you don't understand, that doesn't have tests, that you need to change.

### Demo Gilded Rose
The code for [The Gilded Rose Refactoring Kata](https://github.com/emilybache/GildedRose-Refactoring-Kata) is available in many programming languages. Spend a few minutes explaining the scenario, perhaps get people to read the [requirements](https://github.com/emilybache/GildedRose-Refactoring-Kata/blob/master/GildedRoseRequirements.txt). Mention the new feature that's needed, and the goblin who will get angry if you change his code. 

Show the horrible code, and the lack of tests. Get the initial test to pass, and explain why it's not a very good test. 

Solve the exercise in the best way you know. I use these techniques:

- Combination Approvals
- Coverage
- Mutation Testing
- Normalize Conditional (aka lift-up conditional)
- Replace Conditional with Polymorphism

If you have time, also add the new feature for Conjured items. If you change the goblin's code, explain how you'd handle him.

### Reflect
Ask participants to note down on a sticky note the names of any techniques they saw you using that they would like to learn to use too. Gather the notes and use them as input for planning future learning hour sessions.
