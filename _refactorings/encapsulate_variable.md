---
layout: refactoring
title: Encapsulate Variable
source: Martin Fowler
source_url: https://refactoring.com/catalog/encapsulateVariable.html
code_smells: global_data
learning_hours: primitive_obsession
---

# Encapsulate Variable / Encapsulate Field

* Identify a variable or field that has public or global access that you would like to encapsulate.

## Refactoring steps
* Create a getter and setter function for the field you want to encapsulate. 
  * IDE: with the cursor on the field, Generate... Getter and Setter
* Compile / run static checks.
* Go through each reference to the variable or field and replace it with a call to the getter or setter function. 
  * You could "lean on the compiler" to find all the references - rename the field or variable and find all the places that break.
  * Test after each replacement.
* Change the field or variable to be private (if your language allows).
* Test.

At this point you've succeeded in you original aim - the global variable is encapsulated by getter and setter functions. Follow-up refactorings:

* If you have several related fields, you could Extract Class. Give it a good name.
* Now it is encapsulated, you can more easily change the type of the field. For example [Replace Primitive with Object](replace_primitive_with_object.html).
