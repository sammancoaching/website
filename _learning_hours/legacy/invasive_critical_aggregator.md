---
theme: legacy
title: Invasive Critical Aggregator
kata: murder_mystery
difficulty: 1
author: ronheywood
via: emilybache
---

# Invasive Critical Aggregator

This is one of the "Patterns of Legacy Displacement" from [this article](https://martinfowler.com/articles/patterns-legacy-displacement/)

* 5 min connect: How could you break this Query?
* 10 min concept: Invasive critical aggregator
* 30 min concrete: SQL murder mystery
* 10 min conclusions: Did you solve the puzzle? Who was the murderer?

## Connect
Prepare a screenshot of a SQL query and some results (you could use the first query from the 'concrete' section below). Ask 'In what ways could you change the database so this query would no longer work?' People can raise their hands with suggestions. You're hoping people will say things like - you could change the type of this column, the name of that column, or split out that column into a lookup table, that kind of thing. Almost anything you do to the db schema would break the query.

## Concept
Present the gist of [the article](https://martinfowler.com/articles/patterns-legacy-displacement/) about 'critical aggregator' and why the 'invasive' version is an anti-pattern.

## Concrete - SQL Murder Mystery
This exercise is provided online by [Knight Lab](https://mystery.knightlab.com). The idea is to write SQL queries to expose a murderer using data in their database. You write queries on the webpage to interrogate various tables. While people are solving this, ask them to keep track of the queries they are using.

Before splitting into pairs, demo how to write the first query and find the first piece of data on the road to exposing the murderer. For example write this together:

    Select * from crime_scene_report
    where city = 'SQL City';

Then split into smaller groups to continue from there.

## Conclusions

Invite the group to respond to the concrete excercise - You're hoping that they will have found the murderer and had lots of fun in the process.
As they talk about the excercise, you can spot opportunities to ask questions like:

* As a user of the database what made this database easy to work with? What made it hard?
* What tables did you spot, where you might not own the data you used to solve the murder?
* How much harder would it be to solve the next case, if you were not able to rely on what you had already learned about the structure of those tables?

### Further Reading

The goal of this learning hour is to introduce the idea of the Critical Aggregator pattern, and to consider some causes of the Invasive Critical Aggregator anti pattern.

When encountering challenges caused by Invasive Critical Aggregator the first approach is to create a new implementation of Critical Aggregator, which can be done using  techniques such as [Divert the Flow](https://martinfowler.com/articles/patterns-legacy-displacement/divert-the-flow.html), or combined with other patterns such as [Revert to Source](https://martinfowler.com/articles/patterns-legacy-displacement/revert-to-source.html).

The alternative, more common approach, is to leave the aggregator in place but use techniques such as [Legacy Mimic](https://martinfowler.com/articles/patterns-legacy-displacement/legacy-mimic.html) to provide the required data, during the period that the re-architecture is being worked on.