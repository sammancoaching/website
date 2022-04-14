---
layout: code_smell
title: Data Class
---

# Data Class
The class has fields, ie mutable state, but no other behaviour. There may be get and set methods for the fields, or they may be public. There could be functions elsewhere that operate on this data which could be moved here to make a more object-oriented design.