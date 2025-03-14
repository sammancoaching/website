---
theme: approval_testing_texttest
title: Supplying User Input via stdin
kata: dungeon_escape
difficulty: 1
author: emilybache
affiliation: Bache Consulting
languages: c,texttest
tags: c texttest
---

# Supplying User Input via stdin
Command-line programs sometimes ask the user for input interactively. This is a fun exercise to get the hang of that. You will also practice discovering use cases and turning them into tests.

## Learning Objective
* use TextTest to operate an application with user input
* turn use cases into tests

## Session Outline

* 10 min connect: Discover use cases
* 10 min concept: Supplying standard input
* 30 min concrete: Write tests for Dungeon Escape
* 5 min conclusions: How could you use this?

## Connect - Discover use cases

Give people access to the [Dungeon Escape Refactoring Kata](https://github.com/emilybache/DungeonEscape-Refactoring-Kata) running on a suitable machine. Note - the code is written in C but you don't need to understand C to do this exercise. Get them to begin by running the program in a terminal as a user would, and play the game. Encourage them to try to both win by escaping and lose by being killed.

## Concept - supply input via TextTest
Show them how to create a 'smoke' test first, where there is no input. Then show them how to create another test that just quits as the first thing it does.

## Concrete - write tests for Dungeon Escape
Get them to re-create the two tests you showed in the demo, and go on to create tests for further scenarios. Encourage them to create tests for different scenarios like escaping, getting killed and just wandering around for a long time.

## Conclusions - how could you use this?
[How could you use this?]({% link _activities/conclusions/how_to_apply_here.md %}). Do you have any command-line programs that take user input which you'd like to test?

