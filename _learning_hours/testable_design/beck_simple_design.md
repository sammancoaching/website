---
theme: testable_design
title: Beck's 4 rules of simple design
name: beck_simple_design
kata: fizzbuzz
difficulty: 1
author: emilybache
affiliation: ProAgile
---

Beck's rules of simple design
=============================

In this learning hour we learn about Kent Beck's rules of simple design. There is no 'concrete' part of this learning hour, you don't get to practice using these rules. You should probably follow up this learning hour with a second one where you do so.

There is a YouTube video on Emily Bache's channel for this learning hour - ["You Aren't Gonna Need It: in TDD Design is Simple"](https://youtu.be/OrxqfrTPns0)

## Session Outline

* 5 min connect: vote for favourite design guidelines
* 25 min concept exercise: implement FizzBuzz however you like
* 10 min concept: read FizzBuzz code samples
* 10 min concept: YAGNI and Beck's rules of simple design
* 5 min conclusions: note down how TDD affects design

### Connect - vote for favourite design guidelines
Make a list of plausible design guidelines that people might find important/relevent/useful. Put them up on a shared whiteboard and ask each person to pick their top 4 and mark them with dot votes.

* No duplication
* Single return per function
* Testable (has unit tests)
* Extension points for adding functionality
* Doesn't have unnecessary elements or extension points
* Readable
* Uses naming conventions like m_ for member, I for Interface
* Small classes and methods
* Small memory footprint
* Fast speed of execution

Do include language or organization specific guidelines if you know any good ones.

### Concept exercise
Give them a starting position with an empty failing test and ask them to implement [FizzBuzz]({% link _kata_descriptions/fizzbuzz.md %}). Tell them to do it however they want to, and to follow the design guidelines they want to follow.

If no-one does TDD and they all end up with rather simple but less testable code, you might want to give them a quick demo of what solving FizzBuzz with TDD looks like. You should end up with something more like code sample 3 in the next section. Hopefully you won't have to - the ideal is that some pairs use TDD and end up with code like sample 3, and some don't, and end up with code like sample 1 or 2. That's important for the next section.

### Concept - TDD changes your design
Print out and pin up the code samples from ["FizzbuzzKata-Samples"](https://github.com/emilybache/FizzBuzzKata-Samples) around the walls of the room, in order. Only include the implementations, not the tests. Have people walk around in their pairs and study the code together. Get them to put a marker by the code sample they think is most similar to their own. If you did a TDD demo, ask them to mark the code sample most like the design you came up with as well. 

When everyone's done that, take a whole group discussion. Did those who wrote unit tests end up with a different design than those who didn't? Hopefully there will be examples of both and you can lead them to the insight that doing TDD (or at least writing unit tests) changes your design.

### Concept - Beck's rules of simple design
Explain Beck's rules of simple design. I found a good description of them in [this blog post by Ron Jeffries](https://ronjeffries.com/articles/019-01ff/iter-yagni-skimp/). Explain that in TDD testability is a first class design guideline. Compare Beck's 4 rules with the top 4 voted design guidelines you came up with in the "connect" part of this learning hour. Do you agree with Beck? Do you prioritize something else?

### Conclusions
Ask people to discuss in pairs how TDD could affect your design choices, and if doing it would make you personally re-prioritize.


