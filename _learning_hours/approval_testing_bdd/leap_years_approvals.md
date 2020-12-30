---
layout: learning_hour
title: Leap Years with Approvals
parent: Behaviour Driven Development with Approval Testing
grand_parent: Learning Hours
nav_order: 1
---

# Leap Years with Approvals

The group will probably have seen Leap Years before, so it's a good one for introducing different styles of testing. You'll need to prepare for this session by coming up with a variety snippets of test code, and printing them out in a large font.

People learn better when they are moving about than when they are sitting still. They also learn more when they are talking than when they are just listening. That's why we put the code listings on the wall and have them walk about, talking to one another.

## Session Outline
 
* 5 min connect: in pairs, properties of a good unit test?
* 20 min do: walkabout and assess test snippets  
* 10 min reflect: best/worst tests? Why?  
* 15 min demo: leap years 2 ways - ordinary TDD and TDD in another style   
* 5 min reflect: pairs assess demo tests against their list

### Connect
In pairs, write down 3 properties of a good unit test.

### Do
Have the pairs walk around the room looking at the code snippets you've pinned up on the walls. Have them read the code and try to work out what the test is doing. Assess the test against the criteria they just came up with. Add new criteria as it occurs to them.

Encourage people to circulate and not spend too long on one code snippet. Tell them it's ok to not understand everything about the code, it could be a sign that it has room for improvement.

When everyone has been looking at the code for about 15-20 minutes, bring it back to whole group discussion. At a flipchart or whiteboard, ask people to volunteer what they've learnt. You want to know the criteria they came up with, and which test snippets on the wall are the best/worst. You might find disagreement in the group which could be interesting to know but possibly not helpful to have a big discussion about in a whole group. Try to  focus on what people agree on.

You might want to select some code snippets from the actual codebase the group is working on, if that would not be too sensitive. Otherwise, I have gathered together some test cases in the [Lift-Kata-Sample-Tests repo](https://github.com/emilybache/Lift-Kata-Sample-Tests). The idea of the code snippets is that in your judgement, some are better than others. Some are short, some are long, some contain loops, some have too much detail, some have multiple asserts, some use unfamiliar test frameworks, etc. Have about 4-8 snippets, each one no more than about 20 lines of code.


### Demo
Show the plain vanilla TDD implementation of Leap Years first. Don't forget the first step, which is writing up the four test cases on the whiteboard. Implementing the whole Kata only takes a few minutes, and they will probably have seen it before in a previous session. Show it to them again so they remember better.

Start over from scratch and demo using Approvals.

Since LeapYears is a relatively small problem to solve, probably any other approach than standard TDD looks like overkill. You might want to explain that people should focus on what the approach looks like rather than whether it is appropriate for this problem. You're using a problem they are familiar with so they can focus on something else.

### Reflect
Ask people to discuss in pairs. Do the tests that come from the new approach have all the properties they came up with during the earlier part of the session? Leave your demo code up on the projector screen where they can see it while they discuss.



