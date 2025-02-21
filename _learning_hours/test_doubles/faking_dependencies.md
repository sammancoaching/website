---
theme: test_doubles
title: Faking Dependencies
kata: html_converter
difficulty: 3
author: emilybache
affiliation: ProAgile
---

# Faking Dependencies
Following on from the learning hours on Stubs. Fakes are like stubs but with a real implementation.

### Connect
[Mark the true statements]({% link _activities/connect/pick_the_correct_items_on_the_list.md %}) and not the other ones:
- A stub is a piece of code that doesn’t work yet
- A test double replaces a dependency of the class or function under test
- A stub behaves differently depending on the situation and the arguments it’s passed
- A test double is configured by a unit test to set up a specific situation for the class under test
- When you’re developing an API which another team will consume, you might give them a stub implementation of the API to work against.
- Test Doubles are not used in system testing, only unit testing
- Stubs are re-used in several test cases
- You can use a mocking framework to create both mocks and stubs

### Concept - Fakes
Fakes are like stubs but they actually have a real implementation. Stubs just return hard-coded answers but Fakes do calculations, have state, and behave appropriately. Typical abstractions that you fake are files, queues, iterators, data stores.

### Concrete
[Html Converter](https://github.com/emilybache/HtmlConverter-Kata). First get them to read the code and establish which abstraction you want to replace with a test double. Make sure they have the documentation for the in-memory string version of a file for their programming language. 

* [Python](https://docs.python.org/3/library/io.html) - StringIO
* [Java](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/StringReader.html) - StringReader
* [C#](https://docs.microsoft.com/en-us/dotnet/api/system.io.stringreader?view=net-6.0) - StringReader

Get them to find the documentation for their language if you don't have it.

Remind them to preserve the original constructor in addition to a new one that lets you inject the test double.

### Conclusions
[When should you use]({% link _activities/conclusions/when_to_use_this.md %}) a Test Double? In particular, when should you use a Fake? Make some notes and share with the group.
