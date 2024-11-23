---
theme: testable_design
title: Reading by Renaming
name: naming
kata: theatrical_players
difficulty: 1
author: edytterbrink
affiliation: Chocolate Driven Development AB
---

# Reading by Renaming

It is wasteful to read code that you don't need to change.

If you trust the name of the code, you don't have to read the code itself.
When the code is hard to navigate, and full of surprises,
we don't want nice names, we want useful names.

Well designed code uses contexts and domain to build trust in the naming.
But often it is ill advised to trust the names used in software.
That is when this learning hour comes in handy.

This learning hour is heavily inspired by Arlo Belshee and his work on [Naming as a Process](https://www.digdeeproots.com/articles/naming-process/).
One change is that I call the *honest* step for *honest incomplete* and the *completely honest* for *honest complete*,
to stress to difference between them. 
I also think that the *obvious nonsense* could be called *honest nonsense*,
to contrast it with the deceptive nonsense we see in a lot of code,
but try to stick to *obvious nonsense* here.

We want to store knowledge in the code. 
Naming the code for what it actually does, 
the first time you read it, 
saves the time of re-reading the code.
Descriptive naming can mitigate lack of design,
while the design is worked on.


The new name can then guide remodeling the code.
The end goal is to have a clear language for the code,
that speaks of the domain.
This learning hour is a step in that direction. 

There is a video on Emily Bache's YouTube channel that shows a variant on this learning hour ["Trustworthy Code with Naming as a Process"](https://youtu.be/PPQHJpWG4GA)

## Learning objective
Being able to explain how to give a piece of code a name that can be trusted.

## Connect
Let the group look at some code and say if they think that the name is a good one.
Work in pairs, or small groups, if it is a big team. 

Examples (in some made up language and framework): 

    def getUsers(db){
        return db.get(Users.all);
    }

    def onStart(args){
        Events.register("all");
    }
    
    def saveUser(user, db){
        db.save(user)
        Events.send(UserNotifications.saved(user))
    }


## Concept
Names are important when we want to read less code. 
We often try to name things better than they deserve. 
When it is hard to find a "good" name it is often a sign of poor design.
This is an exercise in exposing lack of structural integrity,
instead of hiding it behind pretty names, that don't tell us what the code does.

Arlo Belshee has the concept
[Naming as a Process]( https://www.digdeeproots.com/articles/naming-process/).

This learning hour is heavily inspired by step two, three and four: *obvious nonsense*, *honest incomplete* and *honest complete*.


1. *Obvious nonsense* is about changing the current dishonest nonsense name to an honest one.
It can also be used when a block of code is extracted, as a part of a refactoring.
2. *Honest incomplete* is a way to improve it to be honest about one thing, 
and state that this is not all there is.
3. *Honest complete* is when everything the code does is covered by the name.

After this we can move on to splitting the code into smaller pieces.
But that is out of scope for this learning hour.

[There is a companion blogpost for this learning hour.](https://www.chocolatedrivendevelopment.com/2022/10/10/whats-in-a-name/)
But I recommend also reading the original posts by Belshee.

## Concrete
There are two exercises, following after each other.
The first exercise is to get a feel for the different stages of naming.
The second is hands on, taking a name from obvious nonsense to honest complete with unfamiliar code.
Show a small demo exercise for each one, before having the team try it.
That is easier than explaining what to do. 
[Sorting names](#sorting-names) can also be used as a connect for a follow up learning hour, 
especially if someone missed this one.

### Sorting names ###

#### Preparations
Create notes for each item in the categories, mix them up and have the team sort them.
Create pairs or small groups for the team to work in. 

#### Tools
- Notes, physical or digital.
- A board to match the notes. The kanban in Miro works well.

#### Instructions for the team
> Sort the following names into categories of *obvious nonsense*, *honest incomplete*, *honest complete*.

#### Names to sort, by correct group
Obvious nonsense:
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

### Name some code  
Give the team a piece of code with a nonsense name. 
A good starting point is the main body of 
[theatrical players kata]({{ site.baseurl }}{% link _kata_descriptions/theatrical_players.md %}). 
Reuse the groups from the previous exercise. 
Ask them to read the code and then edit the name for the function,
step by step, while crossing out parts of the code in the screenshot.
Each iterations should make another part of the code represented in the name,
until there is nothing more to describe. 
If the code can be roughly reconstructed from the method name, the name is detailed enough.
I recommend using a screenshot instead of actual code, not to get distracted by the editor,
or the option to start refactoring. 
It also makes this learning hour possible to do without computers, 
or if remote, without an editor.

#### Tools
- Screenshot of code, printed on a large paper or on a digital board.
- Text area/paper for editing name.
- Ways to hide or mark the code that is represented in the name.

#### Instructions for the team
> Give the code an honest incomplete name. 
> Read the code. 
> Find parts that belong together and add something to the name that represents that part of the code.
> Mark the code represented in the name to remember you processed it.
> Continue until all the code can be roughly reconstructed by reading the name.
> Change the name to signal that it is now complete.

## Conclusions
Pair up and explain how to get to an *honest complete* name and why we want that.
