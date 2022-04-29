---
theme: refactoring
title: Primitive Obsession
kata: person
difficulty: 1
author: agmsytim 
affiliation: Atruvia 
---

# Primitive Obsession

It's useful to have a shared knowledge of different Code Smells and how to handle them. [Primitive Obsession](/reference/code_smells/primitive_obsession.html) is a very common smell which occurs in projects.
In this learning hour we will talk about what it is and how you are able to refactor it. 

## Session Outline
 
* 3  min connect: When does code smell for you? 
* 20 min concept: Explanation of Primitive obsession and why is this a disadvantage? 
* 25 mins concrete: Replace primitive with object
* 10 min conclusion: Reflect on how the participants would describe primitive obsession after the session

### Connect: When does Code smell for you?

* Everybody explains her or his own definition of smelling code.
 
### Concept: Primitive obsession
* Give a definition of primitive obsession
  - The excessive use of primitive data types instead of (small) objects
  - The use of instances to represent information (p.e. Different User Roles: USER_ROLE_ADMIN, USER_ROLE_ENGINEER)

### Why is primitive obsession a disadvantage? (e.g. Why is it a problem?)
* Find together disadvantages of primitive obsession
* Collect them on a whiteboard
  For Example:
  - less readadble code, because less information with missing classes
  - more need for inline comments
  - fields who should be grouped together are not necessary in the same module
  - risk to violate the DRY principle
  - less information hiding

### Concrete: Replace primitive with object
* Give a brief explanation of the process of the 'Replace Primitive with Object'-refactoring from Martin Fowler's Refactoring book and demonstrate them by for example by replacing the id field with a new class. 
  - Encapsulate the variable
  - Create a simple value class for the data value.
  - Copy the field and getter to it
  - Create a constructor with the primitive value of the fiels as parameter
  - Change the field type in the original class
  - Invoke the getter of the new object in getter of the original class
  - Change the setter to create a new value object
* To support the refactoring it is helpful to have some UML-like sketch on a whiteboard which shows how the target relationship between Person and other classes (p.e. Id) will look like.
* Afterwards the participants should try to refactor the class Person on their own. (In pairs or ensemble)
* They should use as much IDE-refactoring-support as possible.

### Conclusion: How would you describe primitive obsession in your own words?
* Close the session with every participant explain primitive obsession in their own words.
