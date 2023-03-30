---
name: primitive_obsession
theme: refactoring
title: Primitive Obsession
kata: person
difficulty: 1
author: agmsytim 
via: emilybache
affiliation: Atruvia 
---

# Primitive Obsession

It's useful to have a shared knowledge of different Code Smells and how to handle them. [Primitive Obsession](/code_smells/primitive_obsession.html) is a very common smell which occurs in projects.
In this learning hour we will talk about what it is and how you are able to refactor it. 

## Session Outline
 
* 3  min connect: What is a code smell? 
* 20 min concept: Explanation of Primitive obsession and why is this a disadvantage 
* 25 mins concrete: Replace primitive with object
* 10 min conclusion: Reflect on how the participants would describe primitive obsession after the session

### Connect: What is a code smell for you?
Everybody explains their own definition of a code smell.
 
### Concept: Primitive obsession
Explain [Primitive Obsession](/code_smells/primitive_obsession.html), for example:
  - The excessive use of primitive data types instead of (small) objects
  - The use of integers or enums to represent types of objects

### Why is primitive obsession a disadvantage?
Ask everyone to come up with disadvantages of primitive obsession, and collect them on a whiteboard.
You're hoping for reasons like these:
  - less readable code, because you get less information with missing domain concepts
  - more need for inline comments
  - fields who should be grouped together are not necessary in the same module
  - risk of violating the DRY principle
  - less information hiding

### Concrete: Replace primitive with object
Give a brief explanation of the process of the [Replace Primitive with Object](https://refactoring.com/catalog/replacePrimitiveWithObject.html) refactoring. 

Using the [Person Refactoring Kata](https://github.com/sammancoaching/Person-Refactoring-Kata), demonstrate replacing a primitive with a more complex type. For example replace the `role` field with a `Role` class. 
  - Encapsulate the variable
  - Create a simple value class for the data value.
  - Copy the field and getter to it
  - Create a constructor with the primitive value of the field as parameter
  - Change the field type in the original class
  - Invoke the getter of the new object in getter of the original class
  - Change the setter to create a new value object 

To support the refactoring it is helpful to have some UML-like sketch on a whiteboard which shows how the target relationship between Person and other classes will look before and afterwards. Then the participants should try to refactor the class Person on their own. (In pairs or ensemble). They should use as much IDE-refactoring-support as possible.

### Conclusion: How would you describe primitive obsession in your own words?
Ask everyone to [explain the main idea](/activities/conclusions/explain_main_idea.html) of primitive obsession in their own words.

# Acknowlegements
This learning hour was first published elsewhere: [Primitive Obsession](https://github.com/atruvia/samman-coaching-website/blob/lh-additions/_learning_hours/refactoring/primitive_obsession.md) 