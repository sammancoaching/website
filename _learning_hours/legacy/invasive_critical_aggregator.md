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

* 5 min connect: How could you break thi
* 10 min concept: invasive critical aggregator
* 30 min concrete: SQL murder mystery
* 10 min conclusions:

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

TODO
