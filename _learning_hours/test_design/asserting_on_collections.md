---
theme: test_design
title: Asserting on Collections of Objects
kata: strange_characters
difficulty: 1
author: emilybache
tags: test_design
---

# Asserting on Collections of Objects
In the Assert part of the test, you often want to check a collection of objects contains the correct elements. 

### Learning Objectives

* Recognize a ValueObject
* Use an assertion that checks the contents of a collection, not only that it has the correct size.

## Session Outline

* 5 min connect: What is the most important job of a unit test?
* 10 min concept: Asserting on Collections of Objects
* 30 min concrete: Strange Characters exercise
* 5 min reflect: What did we learn about test design?

### Connect: Important Job of a Unit Test
Ask "What is the most important job of a unit test"? Collect two or three answers and write them on a shared whiteboard. You're hoping someone will mention that it should fail when there is a problem, and give a good message.

### Concept: Asserting on Collections of Objects
Today we're looking at collections of [Value Objects](https://en.wikipedia.org/wiki/Value_object) so you probably need to first explain what that is. 

Note - this code is taken from "ExampleCharacterTestCase" in the [StrangeCharacters](https://github.com/emilybache/StrangeCharacter-TestDesign-Kata)

Show lines of code like the ones below. Ask whether the final assertion will pass or fail:

    var nancy = new Character("Nancy", "Wheeler");
    Assert.AreEqual("Nancy", nancy.FirstName);
    Assert.AreEqual(nancy, nancy);
    Assert.AreEqual(new Character("Nancy", "Wheeler"), nancy);

Explain that it could pass if Character is a ValueObject but not otherwise.

You could skip the next part of the explanation if you think they will discover what makes a good assertion for themselves during the exercise.

If you have a collection of Value Objects you would like your test to give a good message when the collection has the wrong elements in. These assertions get more and more stringent:

        Assert.NotNull(charactersList);
        Assert.AreEqual(3, charactersList.Count);
        CollectionAssert.Contains(charactersList, new Character("Nancy", "Wheeler"));
        CollectionAssert.AreEquivalent(new List<Character>()
        {
            new Character("Nancy", "Wheeler"),
            new Character("Mike", "Wheeler"),
            new Character("Karen", "Wheeler"),
            
        }, charactersList);
        Assert.AreEqual(new List<Character>()
        {
            new Character("Karen", "Wheeler"),
            new Character("Mike", "Wheeler"),
            new Character("Nancy", "Wheeler"),
        }, charactersList);

The "AreEquivalent" assertion checks the collection has the correct elements, the "AreEqual" assertion checks they are also in the correct order.

You should prefer an assertion that checks the contents, not only the size of the collection.

Note: if your collection is not of ValueObjects then consider using a Printer and Approval testing instead.

### Concrete: Strange Characters
The [StrangeCharacters Test Design Kata](https://github.com/emilybache/StrangeCharacter-TestDesign-Kata) has some code with well-marked bugs in. First show them the code and the one test, that passes.

For each bug:
- Create a new (empty) test case to expose the bug. Write a  good test name that explains what the bug is
- Write the body of the test case: it should fail because of the bug
- Fix the bug: the test case should now pass.

During the exercise hopefully they will discover they need to check the contents of a collection and will want to use an assertion that gives a good error message when there are additional elements or missing elements.

### Conclusions: Test Design
What is important to remember when your test has to check a collection of objects? [Write an important takeaway]({% link _activities/conclusions/write_important_takeaway.md %})
