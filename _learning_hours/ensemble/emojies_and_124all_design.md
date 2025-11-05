---
theme: ensemble
title: Ensemble Emojies and 124All-Design
kata: TBD
difficulty: 1
author: philou
tags: teamwork
---

# Ensemble Emojies and 1-2-4-All-Design

When working as an ensemble, it can be challenging to communicate needs without breaking the flow. In this learning hour, we will explore using simple emoji protocols to signal common needs and practice the 1-2-4-All design pattern to facilitate inclusive design discussions.

## Learning Objectives

By the end of this session, participants will:

1. Understand that ensemble work benefits from lightweight *shared protocols* that support flow and inclusion.
2. Learn the concept of **async, non-blocking back-communication** (signaling without interrupting).
3. Discover and practice basic **emoji protocols** for expressing needs.
4. Experience using **1-2-4-All** (or 1-3-All remotely) as a structured, inclusive design discussion pattern.
5. Leave with one new shared protocol they can immediately apply in their next ensemble session.

## Session Outline

* 10 min connect: Mini 1-2-4-All on Ensemble Communication
* 15 min concept: Emoji Protocols + 1-2-4-All Design
* 30 min concrete: Protocol Experimentation Round
* 10 min conclusions: Adopt and Extend

## Connect: Mini 1-2-4-All on Ensemble Communication

Ask:

> _Look back at the past few days or weeks. When you were working in an ensemble, and was not typing nor talking: remember what are examples of things you would have wished to communicate, without breaking the flow?_

Then:

1. **1 min – Alone:** Think of a moment when you wanted to say or do something *without interrupting*.
2. **2 min – In pairs:** Share examples or ideas of how you could signal that need.
3. **4 min – By pairs of pairs:** Merge ideas and highlight patterns.
4. **All – Share:** Collect on a shared board or chat. Ask one group after the other for the next most important insight.

If remote: use 1-3-all (3 min triplet breakouts) instead.

Debrief:

Highlight the tension between *staying in flow* and *needing to communicate*:

> _Today, we’ll explore simple ensemble protocols that let everyone communicate smoothly — even the quieter voices._

## Concept

### 1. Emoji Protocols

1. Facilitator quickly presents the **emoji set**:

   | Emoji | Intent                 | MS Teams  |
   | ----- | ---------------------- | --------- |
   | ⌚    | Time to switch         | (watch)   |
   | ☕     | I need a break         | (coffee)  |
   | 🏗    | Let’s pause for design | (build...)|
   | 👋    | I need to leave        | (bye)     |
   | BRB   | I’ll be right back     | (BRB)     |
   | ❓    | I need an explanation  | (question) |

2. Demonstrate posting one or two emojis during a simulated mob. Depending on your setting:
    * Remote: post in chat or use reactions. In Microsoft Teams, it works best by posting a single emoji in the chat while readers keep their chat panel closed.
    * Physical: display a label in front of you on your desk.
3. Invite everyone to try one live (post or raise emoji cards).
4. Debrief [popcorn-style]({% link _activities/conclusions/popcorn_feedback.md %}): “How does it feel to signal this way?”

![Example of physical emoji cards](/assets/images/ensemble-emojies-physical.jpg)

### 2. 1-2-4-All Design

1. Explain that when 🏗 appears, the team pauses and runs a short **1-2-4-All design**:
   * 1 min think, 2 min exchange in pairs, 4 min pair of pairs, All merge.
   * Remote version: **1-3-All** (3 min triplets breakout).
2. Remember you practiced this in the connect phase.
3. Debrief [popcorn-style]({% link _activities/conclusions/popcorn_feedback.md %}): “What was different compared to a free-form discussion?”

#### Tips that might be worth sharing

- The inviting question for 124All is really important:
    - make it as concreate as possible
    - make sure everyone understands it
    - you can ask for "the best" or "all" ideas
- Adapt the timings to the complexity of the quesions, but:
    - keep it short
    - it's better to run multiple short rounds than a single long one

## Concrete Practice: Protocol Experimentation Round

Let's practice this on a short ensemble coding task.

Adapt the coding exercise and design question to the team. Here is an example around testing a [log parser](https://github.com/philou/log-parser-kata):

1. Setup the ensemble coding environment.
2. Present the coding exercise: "Someone wrote a log parser, but they forgot to add tests! Your ensemble’s task is to add tests to the log parser while practicing the emoji protocols and 1-2-4-All design pauses."
3. Kick start with 124All-Design. Share the code so that everyone can browse it (ex: https://github.com/philou/log-parser-kata/blob/main/python/log_parser.py), and ask the question: "Read this code and list the tests we should write around it. Don't just write down a list of ideas, use real good (test names)[../test_design/test_names.md]."
4. Collect the test names as comments in the test file, asking one group after the other for 1 more test name.
5. Start the ensemble, now implementing these tests
6. Invite everyone to use the emoji protocols during the mob: ⌚, ☕, 🏗, 👋, BRB, ❓. Model the use of emojis as needed. (It's ok to exaggerate!)
7. Debrief as a group using the popcorn method:
    * What felt easier or smoother?
    * Did the emojis help keep the flow?
    * How did the design pause feel compared to normal discussions?

## Conclusion: Adopt and Extend

Ask:

1. Ask the team members if they are ok to commit to trying these protocols (the emoji set and the 1-2-4-All design pause) for our next few ensemble sessions?
2. You can also ask "Is there one additional signal your team would like to try?”. Use the same 1-2-4-All pattern to brainstorm a unique new signal to try. Write it on a shared list and take a screenshot or photo to keep.

Wrap-up reflection:

> _Ensemble work improves when we make communication visible and lightweight. These small shared signals help everyone contribute without breaking the flow._
