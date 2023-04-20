---
title: Strange Characters
kata_name: strange_characters
---

# Strange Characters

You have a datastructure containing Character objects. The exercise is to find particular Characters given various criteria. 

A Character has the following attributes:

* First name - string (must be defined and unique in the datastructure)
* Family name - string (optional)
* whether they are a Monster or not - boolean (must be defined)
* Nemesis - Character (optional)
* Parent - Character (optional)
* Children - collection of Characters (optional)
* Siblings - collection of Characters (optional)

You should be able to search a datastructure of Characters using the following criteria:

* Find by first name - return one Character
* Find the parent of a given Character - returns one parent
* Find all Monsters - return all the monsters.
* Find family by name - return all Characters with the given family name.
* Find family by character - return all Characters with a parent or child or sibling relationship to the given character.


Additional Requirements
------------------------
Write a parser that can accept a json file with character data and create a datastructure of all the Characters it contains. 

In addition, implement a new Find method. Find by "character path" - a string a bit like an xpath that will identify a Character in a datastructure.

* /Parent/Child - return the Child of Parent
* /FamilyName:Parent/FamilyName:Child - return the Child of Parent, both should have the given family name.
* /Parent/Child{Nemesis} - return the Nemesis of the given Child character.


There is some sample test data and buggy implementation of the first set of requirements in [StrangeCharacters-TestDesign-Kata](https://github.com/emilybache/StrangeCharacters-TestDesign-Kata). 

There is a sample json file and implementation including the additional requirements in [StrangeCharacters-Refactoring-Kata](https://github.com/emilybache/StrangeCharacters-Refactoring-Kata)