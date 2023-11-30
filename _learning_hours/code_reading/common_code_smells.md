---
theme: code_reading
title: Common Code Smells
kata: tennis
difficulty: 2
author: emilybache
---

# Code Reading - Common Code Smells
Code Smells by definition should be easy to detect. We'll practice looking for them. This learning hour is still being worked on and currently only has a 'concrete' and 'conclusion'.

### Code reading practice
Have people work in pairs to review some code and note down any code smells they find. In particular, they should look for the common smells you just explained. The idea is just to read the code and identify smells, not do anything about it. Note that you can identify code smells without necessarily understanding the code or being able to safely change it.

Example katas that work well:

* Tennis1, Tennis2 or Tennis3 in [The Tennis Refactoring Kata](https://github.com/emilybache/Tennis-Refactoring-Kata)
* [Theatrical Players Refactoring Kata](https://github.com/emilybache/Theatrical-Players-Refactoring-Kata).
* [Gilded Rose Refactoring Kata](https://github.com/emilybache/GildedRose-Refactoring-Kata)

Ask them to work in small groups looking for smells. Give them a printout of the code that they can write notes on or attach sticky notes to. After a timebox of about 10 minutes, ask them to share what they have found. Tell them the 'official' names for smells if they don't know them.

Repeat with another code sample or however many you have time for.

You are hoping that they will find smells like these:

* Tennis1: [Long method](/code_smells/long_function.html), [Heavy Indentation](/code_smells/heavy_indentation.html)
* Tennis2: [Duplicated code](/code_smells/duplicated_code.html)
* Tennis3: [Mysterious names](/code_smells/mysterious_name.html)
* Theatrical Players: [Variable with Long Scope](/code_smells/variable_with_long_scope.html), [Loop](/code_smells/loop.html)
* Gilded Rose: [Long function](/code_smells/long_function.html), [Heavy indentation](/code_smells/heavy_indentation.html)

### What code smells does your production code often suffer from?
Are any of these smells common in your production code? Or are there other smells? Discuss in pairs and note down names of smells you have noticed in your production code. Collect the names on a shared whiteboard.

In the coming days as you work with your production code, keep a look out for smells and note where you find them. 

