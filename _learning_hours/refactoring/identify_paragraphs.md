---
theme: refactoring
name: identify_paragraphs
title: Identify Paragraphs in Long Methods
kata: BigDiceGame
difficulty: 2
author: isidore
via: emilybache
tags:  refactoring legacy
---

# Identify Paragraphs in Long Methods

[Long function]({% link _code_smells/long_function.md %}) is a common code smell. Learning to identify paragraphs that can be extracted as methods is often a good strategy in this situation. This learning hour is about understanding concepts and people will probably not be able to use this technique fluently without a follow-up session. It is adapted from a longer session that is detailed [in this repo](https://github.com/LearnWithLlew/RefactoringToCleanerCode.Slides).

There is a video and other materials available for this learning hour as part of a [Technical Coaching Programme]({% link training/full_package.md %})


## Learning Goals

* Recognize paragraphs in a long method
* Identify paragraphs that you can do 'extract method' on (that have a single return value)
* Recognize when you know enough to give an extracted method an honest name

## Session Outline

* 5 min connect: Discuss: Why does code have long methods?
* 15 min concept: What is a paragraph, how do you spot them
* 25 min concrete practice: Identify paragraphs, extract them, name them
* 5 min conclusion: Explain the main idea

### Connect - Why does code have long methods?
Ask this question and write down what they say on sticky notes on the shared whiteboard. Most developers have experience of and opinions about long methods. There are no wrong answers! 

### Concept - Code Paragraphs
Long methods tend to get longer, (hopefully in the Connect someone will have said this, and you can reiterate what they said). At some point the method may become so long and complex that nobody understands what it does anymore - they can't hold in their head all that complexity at once. In this situation we need techniques that still work even when we don't understand the code.

A [Sparrow Deck](http://llewellynfalco.blogspot.com/p/sparrow-decks.html) is a way to train the brain to recognize patterns. If you havn't done one before with the team, start with the original sparrow deck first. Then show the [Sparrow Deck on Paragraphs](https://docs.google.com/presentation/d/0B5pFqRaidolKZWxoZ0RYckVTeWc/edit?rtpof=true&sd=true&resourcekey=0-ZD9vSBjMxrf2xiVI1mEemQ). 

Alternatively, if you don't want to use these prepared materials, you could collect some of your own code samples and put boxes around parts which may or may not be paragraphs. Give them to participants and ask them to classify them as "paragraph" or "not a paragraph" just by looking.

A [code paragraph]({% link _code_smells/paragraph.md %}) is a section of code within a long method that hangs together and might make sense to extract as a method.

Once you think you've spotted a paragraph, it may take a little more investigation to see whether it really would be possible and/or desirable to extract as a method. If you have a refactoring tool, it can do this analysis for you. Ask it to do "extract method" on the paragraph. It should be able to show you if it's possible and what the method signature would be.

## Concrete Practice - BigDiceGame
Bring up a development environment with a piece of code that has some easy to spot paragraphs that will easily turn into extracted methods. For example [BigDiceGame](https://github.com/LearnWithLlew/RefactoringToCleanerCode.cpp/blob/main/tests/YourCodeGoesHere.h).

Work in an ensemble, guiding the group to convert each paragraph into a method. Use nonsense names at first (AppleSauce) until you are able to come up with honest names. (This is [Naming as a Process](https://www.digdeeproots.com/articles/naming-process)).

## Conclusions - main idea
In pairs, ask people to [explain the main idea]({% link _activities/conclusions/explain_main_idea.md %} ) of code paragraphs.




