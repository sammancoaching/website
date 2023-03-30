---
layout: code_smell
title: Speculative Generality
source: Martin Fowler
---

# Speculative Generality
Extra code and hooks and special cases to handle things that aren't (yet) required. Someone thought that you would need this code to support additional functionality that hasn't been built yet. Often this code has been around for years and no-one has needed it yet.

Sometimes you can spot this code when the only users of it are in a test case. Sometimes your IDE will be able to highlight parameters that aren't used as well as other kinds of dead code.
