---
theme: code_reading
title: Code Reading Tennis4
kata: tennis
difficulty: 1
---

# Code Reading Tennis4

This code has several classes and interfaces but only one public class and two public methods. What to refactor is not immediately obvious so it's useful to do a code reading session on it before trying the refactoring in a subsequent session.

## Learning Goals
- practice 'scanning' code
- recognize that people read code differently
- recognize duplication
- recognize a design pattern "Chain of Responsibility"

## Session Outline

* 5 min connect: Describe situations when you need to read code
* 10 min concept: Code reading eye-tracking research
* 35 min concrete: code reading exercises
* 5 min conclusions: takeaways

### Connect

What are typical situations when you need to read and understand code that you haven't seen before?

As people to note down answers to this question in a shared whiteboard/document. Hopefully they will identify lots of different situations. This is actually a big part of a developer's job.

### Concept - what the eye-tracking research has found
The first concept is 'scanning' code. This is a behaviour researchers observed and wrote up in [this paper](http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.98.1585&rep=rep1&type=pdf). They used eye-trackers to observe developers reading unfamiliar code and looking for a bug. They found the people who were most effective at finding bugs will spend more time in this behaviour they call 'scanning'. That is where the eye rapidly moves over the code vertically taking in many lines. Occasionally the eye pauses on one or two lines and reads them more carefully before continuing rapidly downwards. The lines they tend to pause on will correspond to interesting features like function headers.

The second concept is that novices read code differently from experts. In [this paper](https://researchonline.gcu.ac.uk/ws/portalfiles/portal/24953094/ICPC2015_authors_version.pdf) the researchers use eye-tracking software to compare two groups. In one group the developers were almost complete novices, only having had a few lessons in programming. In the other group they were professional developers with more than 5 years experience. They compared the way their eyes moved over code as they read it. They found important differences. 

A couple of interesting quotes from that paper: "experts read the code less linearly than novices". Although they didn't say this explicitly in the paper I interpret that as meaning they 'scan' more often whereas novices tend to read every line. Another quote: "experts are better able to focus on the relevant source code elements than novices", and they later comment "one of the effective ways to improve skill acquisition is to cue visual attention of novices to the locations that experts attend [to]".

So that's what this session is about. Can we get better at 'scanning'? Perhaps some of us are better at picking out relevant source code elements than others. Can the rest of us learn to do that by finding out what it is they see?

### Concrete code-reading exercises

Print out the code for TennisGame4 from the [Tennis-Refactoring-Kata](https://github.com/emilybache/Tennis-Refactoring-Kata) in the programming language of your choice. (Note, it's not available in every language yet and I welcome pull requests with translations!) Print it in colour with syntax highlighting. Make a copy for each person attending the learning hour.

If it's a remote meeting, put many copies of a pdf printout on a shared whiteboard like Miro. Don't hand out or reveal the code to the participants until you have given them the first instructions below.

#### First glance - scanning

Spend only one minute scanning the code - we want your first reactions

* Note the first thing that catches your eye
* Note the second thing that catches your eye
* Take the remaining time to think about _why_ you noticed those things first.

At the end of the minute, debrief. If it is a small group get each person to explain their two things verbally. With a bigger group, have them write notes then you can pick out the most interesting ones that you ask people to explain verbally. Then ask these questions:

* What lines or facts or concepts were chosen by everyone vs only a few people?
* How do those initial observations help with deciding what to look at next?

We're trying to help people to quickly pick out important elements in the code.

#### Grouping in the code

Now we are going to read the code again, this time looking for groups of elements. If you're using a remote whiteboard, make sure everyone knows how to use the virtual pen and highlighter before proceeding. 

* Mark any public elements in Purple (elements that can be accessed from outside this module/package)
* Find groups of things, choose different colours and mark them.

At the end of 3-5 minutes on this activity, take a look at the markings on each copy of the code. 

* What public elements did we all find? Is there anything we disagree on?
* What groups of classes and interfaces did we find? Is there anything we grouped differently?
* What parts of the code seem to warrant more attention?

During this debrief you could explain the design pattern "Chain of Responsiblity" and which classes form part of that pattern in this code. You could explain that by grouping elements and identifying a design pattern we are practicing 'chunking' - a technique that lets us hold more information in our heads at once.

#### Refactoring targets

Now we're going to read the code a third time, this time looking for refactoring targets.

* Circle refactoring targets in Dark Red
* Look for duplication, functionality that belongs elsewhere, or anything suspect.

At the end of 3-5 minutes on this activity, take a look at the markings on each copy of the code. 

* Is there anything we all found?
* Is there anything that was obvious to one person and not everyone else? What led them to see that thing?

As the coach/facilitator, if you have noticed something in the code that you think is a refactoring target but that nobody else mentioned, you could bring it up during this debrief.


### Conclusions

What have you learnt today about scanning code? How can you get better at it?

Answer this question either by writing sticky notes on a shared whiteboard or by explaining verbally to one another in pairs.

