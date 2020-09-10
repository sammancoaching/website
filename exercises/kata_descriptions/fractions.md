---
layout: default
title: Fractions
parent: Kata Descriptions
grand_parent: Exercises
nav_order: 9
---

Fractions
==========

Write a program that implements the addition of fractions. eg:

1/2 + 3/4

should give:

1 1/4

Constraints
------------

A fraction is a [Value Object](https://martinfowler.com/bliki/ValueObject.html) that is, once created it can't be updated or mutated. The 'add' operation should return a new fraction representing the sum.

When you add two fractions, the result should be expressed in the most reduced form. For example you should give:

3/5

not

6/10
