---
theme: small_steps
title: Take Smaller Steps
kata: rpg_combat
difficulty: 3
author: emilybache
---

# Take Smaller Steps

Inspired by Mike Hill's "Many more, much smaller steps".

## Session Outline
 
* 5 min connect: advantages of incremental releases
* 10 min concept: definition of a step and an action
* 35 min do: RPG Combat kata  
* 5 min reflect: Size of step when delivering? When coding? When practicing?

### Connect
What are advantages to releasing new software once a week rather than all at once in 6 months' time? Gather input from the group on notes, then read them out.

### Concept
A _Step_ takes you from a Ready state to another Ready state. This is different from an _action_ which may begin or end in a non-ready state. A Step can comprise one action or many, but usually it's many. The amount of time it takes to complete a Step is called your _stride length_

When your software system is in a "Ready" state, that means you can deliver it to end users. Often that means it has passed a lot of automated tests and probably had some other kinds of testing too. If you aim to deliver software once a week, you will need it to be in a Ready state with passing tests at least that often. The "stride length" would have to be a week or less.

When your code is in a "Ready" state, that means you can share it with your colleagues by pushing it to a shared branch in version control.  Often that means it both compiles, passes all the unit tests, and possibly some other tests too. If you are doing Continuous Integration, then you need to push at least once per day, so your stride length should be less than one day. 

Mike Hill has a good description of the difference between a Step and an Action in ["MMMSS A Closer Look At Steps"](https://www.geepawhill.org/2021/10/26/mmmss-a-closer-look-at-steps/)

There are lots of benefits to having a shorter stride length. Mike Hill describes many of them in ["MMMSS - The Intrinsic Benefit of Steps"](https://www.geepawhill.org/2021/11/16/mmmss-the-intrinsic-benefit-of-steps/)

### Concrete: RPG Combat Kata
In the [RPG Combat exercise](/kata_descriptions/rpg_combat.html) we will be working on several user stories. After each user story, the code will be ready to ship to end users. However, we want there to be several smaller steps in between where the code has passing unit tests and is ready to share with other developers.

Work on the problem in pairs, taking note of each time you complete both kinds of step. You want to track how many steps you take for each user story, so you can measure your stride lengths. It might be convenient to use cyber-dojo because it allows you to visualize this.

### Conclusions:
Work out how many minutes your steps were during the exercise, both for tests passing to tests passing steps and completed user story to completed user story steps. Estimate your stride length for your normal work, both for pushing to version control and code ready to release. What can you do to shorten your stride length?


