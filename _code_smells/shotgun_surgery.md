---
layout: code_smell
title: Shotgun Surgery
name: shotgun_surgery
source: Martin Fowler
---

# Shotgun Surgery
This is not so much something you can see from reading the code, rather it's something that happens when you try to change the code. You call it 'shotgun surgery' when you want to change one thing and it ends up you have to make a lot of additional changes before the original thing is working properly. It's particularly bad if the additional changes are all over the place and you're not sure if you missed some.

This code smell does actually stem from a design problem though. Things that change together should be put together. If you have to make a lot of edits all over the place to make one logical change then it's a sign your design is has a coupling problem.

Note: this is similar but different to [Divergent Change](divergent_change.html) which is a sign your design has a cohesion problem.
