---
layout: code_smell
title: Message Chains
source: Martin Fowler
---

# Message Chains
When a client asks one object for another object, then for another object, and another object down a chain. It might look like `A.getB().getC().getD().getE()` in a language like Java. It can be quite fragile if there is any change to the structure of an object in the chain - the change propagates and can have wider effects than you'd like. This smell is what you get when you break the [Law of Demeter](https://en.wikipedia.org/wiki/Law_of_Demeter).
