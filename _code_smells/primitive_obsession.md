---
layout: code_smell
title: Primitive Obsession
---

# Primitive Obsession
When you use plain built-in primitive types like `string`, `int`, `float` etc. It can be a sign you should have classes to represent domain concepts like money, co-ordinates, ranges, telephone numbers etc. If you use primitives you risk mistakes like adding inches to centimeters, or not being able to consistently display a phone number with or without its international code.