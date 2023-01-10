---
theme: testable_design
title: Refactor by renaming 
name: naming
kata: theatrical
difficulty: 1
author: edytterbrink
affiliation: Chocolate Driven Development
---
# Refactor by renaming

Reading code you don’t have to change is waste.
Names that are honest and complete can mitigate lack of design,
while the design is worked on. 
Show a small demo exercise for each one.

## Learning objective
Know what steps to take to get a name that can be trusted.

## Connect

Collect "Most unexpected thing a method did, judging from its name."
Work in pairs or as a group, depending on group size. 


## Concept
Names are important if we want to read less code.
”Don’t hide bad design behind pretty names.”
When it is hard to find a "good" name it is often a sign of poor design.

Arlo Balshee has the concept
[7 stages of naming]( https://www.digdeeproots.com/articles/c/series/).

This learning hour covers step two, three and four of those.
They are honest nonsense, honest incomplete and honest complete.


Step one, nonsense is unmasking the name that already is nonsense,
only making it dishonest nonsense.
Honest Nonsense is better than deception.
Then you improve it to be honest about one thing, 
and state that it is not all there is.
When everything is covered in the name and it is complete,
we can move on to splitting it in smaller pieces.
But that is another exercise.

[There is a blogpost where I explain it in my words.](https://www.chocolatedrivendevelopment.com/2022/10/10/whats-in-a-name/)

## Concrete
### Active review
Sort nonsense, honest incomplete, honest

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
Look at code and edit the name for the function,
while crossing out parts of the code on Miro.

Tools:
- Screenshot of code.
- Textfield/paper for editing name.
- Ways to mark the code that is represented in the name.


## Conclude
Write down these steps and practice to use them when you get stuck when naming. 
