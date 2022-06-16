---
layout: code_smell
title: Middle Man
source: Martin Fowler
---

# Middle Man
A class that doesn't do much more than forward all the calls to another class, with little or no behaviour of its own. It could be a sign the clients of this class should talk directly with the class all the calls are fowarded to.