---
theme: testable_design
title: Reading by renaming
name: naming
kata: theatrical_players
difficulty: 1
author: edytterbrink
affiliation: Chocolate Driven Development
---

# Reading by renaming

It is wasteful to read code you don't need to change.

If you trust the name of the code, you don't have to read the code itself.
If the code is hard to navigate, and full of surprises,
we don't want nice names, we want useful names.

In well designed code the context and the domain will help us trust the names of the code.
But often it is ill advised to trust the names used in software.
That is when this learning hour comes in handy.


Naming the code for what it actually does, 
the first time you read it, 
saves the time of re-reading the code.
Descriptive naming can mitigate lack of design,
while the design is worked on.


The new name can then guide remodeling the code.
The end goal is to have a clear language for the code, that speaks of the domain.
This learning hour is a step in that direction. 

## Learning objective
Know what steps to take to give a piece of code a name that can be trusted.

## Connect

Ask the group for "Unexpected things found in a method or function."
Have them tell each other in pairs or each in turn as a group, depending on group size. 


## Concept
Names are important, if we want to read less code. 
We often try to name things better than they deserve. 
When it is hard to find a "good" name it is often a sign of poor design.
This is an exercise exposing lack of structural integrity,
instead of hiding it behind pretty names, that don't tell us what the code does.

Arlo Balshee has the concept
[7 stages of naming]( https://www.digdeeproots.com/articles/c/series/).

This learning hour is heavily inspired by step two, three and four of those.
The steps are *honest nonsense*, *honest incomplete* and *honest complete*.


1. *Honest nonsense* is about changing the current dishonest nonsense name to an honest one.
It can also be used when a block of code is extracted, as a part of a refactoring.
2. *Honest incomplete* is a way to improve it to be honest about one thing, 
and state that this is not all there is.
3. *Honest complete* is when everything the code does is covered by the name.

After this we can move on to splitting the code into smaller pieces.
But that is out of scope for this learning hour.

[There is a companion blogpost for this learning hour.](https://www.chocolatedrivendevelopment.com/2022/10/10/whats-in-a-name/)
But I recommend also reading the original posts by Balshee.

## Concrete
There are two exercises, following after each other.
The first exercise is to get a feel for the different stages of naming.
The second is hands on, taking a name from honest nonsense to honest complete with unfamiliar code.
Show a small demo exercise for each one, before having the team to try.
That is easier than explaining what to do.
The active review can also be used as a connect for a follow up learning hour, 
especially if someone missed this one.

### Active review
Sort the following into categories of *honest nonsense*, *honest incomplete*, *honest complete*.
Create notes for each item in the categories, mix them up and have the team sort them.
Work in pairs or small groups. 

#### Tools
- Notes, physical or digital.
- A board to match the notes. The kanban in Miro works well.

#### Names to sort, by correct group
Honest nonsense:
- Applesauce
- Chutney 
- Sauerkraut 
- Ketchup

Honest incomplete:
- GetBestOffersAndUpdateSomething
- ParseJSONToUsersAndThenSome
- CalculateDistanceAndPutInTheCloudPerhaps
- LayoutSubViewsButThereIsMore

Honest complete:
- GetMatchingRecipeAndUpdateShoppingListIfFriday
- LayoutSubviewsUnlessLegacyPhoneThenLoadLegacyView
- SetGradientUnlessShapeFactoryMissingThenUseDefault
- FindAllUsersAndEveryMonthBackupAllData

### Try it yourselves  
Give the team a piece of code with a nonsense name. 
A good starting point is the main body of 
[theatrical players kata]({{ site.baseurl }}{% link _kata_descriptions/theatrical_players.md %}). 
Ask them to read the code and then edit the name for the function,
step by step, while crossing out parts of the code in the screenshot.
Each iterations should make another part of the code represented in the name,
until there is nothing more to describe. 
If the code can be roughly reconstructed from the method name, the name is detailed enough.
Using a screenshot instead of actual code is not to get distracted by the editor,
or the option to start refactoring. 
It also makes this learning hour possible to do without computers, 
or if remote, without an editor.


#### Tools
- Screenshot of code, printed on a large paper or on a digital board.
- Text area/paper for editing name.
- Ways to hide or mark the code that is represented in the name.


## Conclude
Write down these steps and practice to use them when you get stuck when naming,
or when figuring out what the code in front of you actually do. 
