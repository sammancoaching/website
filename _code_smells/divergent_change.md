---
layout: code_smell
title: Divergent Change
source: Martin Fowler
---

# Divergent Change
This is not so much something you can see from reading the code, rather it's something that happens when you try to change the code. You call it 'divergent change' when lots of different kinds of changes all affect the same module or class. You would prefer to have a design where you can go in and make a change without having to take into account a lot of other code nearby that doesn't need to change. 

This code smell does actually stem from a design problem though. Divergent change is a sign that module or class is not cohesive enough.

Note: this is similar but different to [Shotgun Surgery](shotgun_surgery.html) which is a sign your design has a coupling problem.