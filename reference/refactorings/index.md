---
layout: refactorings_index
title: Refactorings
---

# Refactorings

This is a collection of descriptions of [Refactorings](https://refactoring.com/). The descriptions are original to this site although many of the names are taken from Martin Fowler's book "Refactoring" 2nd Edition.

## Refactoring structure
Each refactoring is described using the structure "Examine - Prepare - Implement - Clear". This is based on the [EPIC Continuous Improvement Cycle by Bryan Beecham](https://www.agilealliance.org/resources/videos/epic-refactoring-applying-the-epic-continuous-improvement-cycle/). I also included a "Follow up" step at the end giving some ideas about what additional refactorings might now be enabled.

* **Examine** - find the program element(s) you want to transform. (AKA _Identify_).
* **Prepare** - before you do the transformation, work on making that change easier. This can mean researching the impact of the planned change, or doing some preparatory refactorings to make it easier.
* **Implement** - follow safe steps to complete the design transformation. (AKA _Refactor, Improve_).
* **Clear** - remove any preparations or scaffolding that is not needed now the refactoring is completed. (AKA _Clean_).

## IDE Support
In some cases the refactoring descriptions includes references to ways your IDE can help you do them more safely. This is intended to help you use your tools better, but be warned - IDEs differ in details and are frequently updated. Descriptions may not always be entirely correct. If there is a note your IDE can help you but yours doesn't seem to do that, look around the menus and see if the assistance is there just under another name.

In the JetBrains family of tools I recommend looking in these three menus when you right click on a program element:
* "Context Actions".
* "Refactor This" - also available on the top level "Refactor" menu.
* "Generate" - also available on the top level "Code" menu.

Once you've found the option you want, I recommend learning the keyboard shortcut for it.
