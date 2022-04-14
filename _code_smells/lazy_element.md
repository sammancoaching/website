---
layout: code_smell
title: Lazy Element
---

# Lazy Element
Unneeded structure that could easily be inlined without losing anything important. For example a function that is named the same as the code in its body. Sometimes lazy elements arise as a result of refactoring - functionality is moved elsewhere and what's left isn't worthwhile any more. Sometimes it comes about as a result of [Speculative Generality](speculative_generality.html) and you now realize it will never be needed.