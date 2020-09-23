---
layout: default
title: Start with the Assertion
parent: Test Design
grand_parent: Learning Hours
nav_order: 2
---

# Start with the Assertion

Tests usually have the structure Arrange - Act - Assert. If you write the test case in reverse order, starting from the assertion, it can help you to design it better. For example, you avoid overdesigning the setup, only create the things you need. Hopefully during this session the participants will discover some other advantages too.

## Session Outline
 
* 10 min connect: sticky notes of key concepts the group should know already  
* 5 min demo: start with the assert
* 30 min do: Mars Rover or Tennis
* 5 min reflect: observations

### Connect
In advance of the session, write sticky notes with some concepts they should already be familiar with, and stick them where everyone can see them on a whiteboard or flipchart. For example you could have these:

- Red, Green, Refactor
- TDD Golden Rule
- Arrange, Act, Assert
- Triangulation
- Overdesign
- Test List
- Ctrl-Shift-R (Or whatever keyboard shortcut brings up the 'Refactor This' menu in your IDE)

Ask the group to gather around the stickies. Ask for a volunteer to step forward, pick up a note and explain what it is. Use coaching questions to help them to explain the important and relevant aspects of the thing, without you taking over the explanation. When the note is explained, move it to one side. Repeat until different people have explained each note.

### Demo: start with the assert
Write a starter test case for the chosen kata, starting with the assertion.

Choose a kata where there is some setup and it's hard to write the whole test on one line. For example Tennis and Mars Rover both need some kind of class which you 'Arrange' into an initial state, before you 'Act' and call a method on it, then 'Assert' the result of the method or the state of the class.

### Do: Mars Rover or Tennis
Practice writing new test cases starting with the assertion and working back to the setup.

### Reflect: Observations on starting with the assertion
Discuss with your pair your observations about your TDD session and specifically the effect it has when you begin by writing the assertion. Note down observations on sticky notes and give the notes to the facilitator.

To trigger more specific observations, you could write up this list of areas on a whiteboard or flipchart at the front:

- Test Structure (Arrange-Act-Assert)
- Test Readability
- Duplication between test cases
- Navigation/Communication
- IDE/Editor

Read out some or all of the observations and stick them next to the relevant area. Create more areas as needed.

The aim is to get people to see that writing the assertion first will help them to succeed with many of the concepts we went through in the 'Connect' part of today's learning hour.
