---
layout: code_smell
title: Temporary Field
---

# Temporary Field
A class has a field which is only set in particular circumstances. At other times it may be empty or null. It can be a sign you should move this field to another class where it will be set all of the time. Also move any functions that use this field.