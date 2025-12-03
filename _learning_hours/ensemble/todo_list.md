---
theme: ensemble
title: Keeping a Shared Indented TODO List
kata: supermarket_receipt
difficulty: 1
author: philou
tags: teamwork
---
# Keeping a Shared Indented TODO List

- **Theme:** Shared Attention and Flow in Ensemble Programming
- **Duration:** ~60 minutes
- **Level:** Intermediate — teams already working as pair or ensemble

## 🎯 Learning Goals

By the end of this session, participants will learn:

1. To keep a **living TODO.md** that reflects what the ensemble intends to do next.
2. To maintain it **while coding**, especially during multi-step refactorings.
3. How it relieves **cognitive load and improves alignment**.
4. That updating the list is **communication and supports baby-step commits**.

## 1️⃣ Connect: Mental Load & Forgetting Things (10 min)

Ask:

> _In the last few days, in ensemble or pair, how did you keep track of what was left to do?_

Use [1-2-4-All]({% link _activities/conclusions/1-2-4-all.md %}) and write down group answers.

Bridge:

> _We’ll explore a simple tool to reduce all that: an **indented TODO list** that becomes the team’s shared working memory._

## 2️⃣ Concept: Show, Don’t Tell (5 min)

Explain that an **Indented TODO List** is about:

* Adding a `TODO.md` or `todo.txt` file in the code
* Always keeping open and visible beside the code.
* Typist updates it in real time.
* Indent subtasks (for example for multi-step refactor).
* Strike through or check items as you finish.
* Supports regular small commits.
* Reorganize freely: it’s a living plan, not a backlog.

Show an example, such as:

```markdown
# TODO.md - Bowling Game kata (example)

- [x] Create Game class
  - [x] Add roll(pins) method
  - [x] Add score() method returning 0 initially
- [x] Handle simple rolls (no spares or strikes)
- [ ] Support spare scoring
  - [ ] Add bonus for one following roll
  - [ ] Update test to cover spare in frame 5
- [ ] Support strike scoring
  - [ ] Add bonus for next two rolls
- [ ] Refactor duplicate scoring logic in spare/strike handling
- [ ] Add test for perfect game (all strikes)
- [ ] Clean up: rename variables to be more intention-revealing
```

Ask:

> _Intuitively, what could be the benefits of such a practice?_

Use the [popcorn share]({% link _activities/conclusions/popcorn_feedback.md %}) to collect answers, write them down.


## 3️⃣ Concrete: Shared TODO in Action (35 min)

### Setup

Provide a **small but multi-step refactoring exercise**. If you run this learning hour after the [Decider Learning Hour]({% link _learning_hours/ensemble/decider.md %}) the team should have come up with a list of improvements to add to the [Uglified Tests Supermarket Kata](https://github.com/philou/Supermarket-TestDesign-Kata/tree/ugly_tests). If you did not, you can still use this kata, here are TODOs to start with:

```markdown
# TODO.md

- [ ] Refactor to test 1 thing per test
- [ ] Remove dead code (2 tests at the end)
- [ ] Investigate and fix line 129
- [ ] Add logging

## Parking

```

Otherwise, other refactoring katas will do, but be mindful of the time it takes for the group to land in the codebase, come up with a few TODO items, start coding, in just 30 minutes.

### Mini-demo

- Create an empty `TODO.md`
- Put it in a tab that is always visible on your screen
- add the above TODO items
- Start working on the first one
- add sub-TODOs as you discover them
- check the items as you finish them
- and commit at every step

If you have the opportunity, move an item to the Parking section, explaining that it's handy to keep track of something that you might decide to do later, but that is not on the critical path right now.

Keep the demo short so that participants have time for practice

### Practice Activity flow

In Pairs:

1. **Initialize the TODO.md**: create a new file and add the above items
2. **Study the code**: to identify next few (sub-)steps and update the TODO.
3. **Code**: as you complete a step, strike it through or mark it `[x]` and commit.
4. **Review or reorganize the TODO** at any moment if new ideas emerged or if something got dropped.

### Facilitation Notes

* Keep the example small enough that they can finish a few steps in 20–25 min.
* Insist that the **typist maintains the TODO**, this keeps everyone synchronized.
* Highlight the communication effect: anyone joining mid-ensemble can read `TODO.md` and immediately catch up.
* Encourage striking through completed items with joy. For example, use Video Conference tools reaction 🎉.
* If someone suggests dropping a task, celebrate!
* Encourage moving optional items to the Parking

## 4️⃣ Conclusions: Reflect and Commit (10 min)

First ask for feedback and thoughts:

> “What changed in our focus when we kept an external TODO.md? What else did you notice?”

Collect and write down answers.

Then ask:

> “How could we start using this in our real work?”

Optionally, you can use a [1-2-4-all]({% link _activities/conclusions/1-2-4-all.md %}) to collect propositions, and run the [Decider Protocol]({% link _learning_hours/ensemble/decider.md %}) to agree on the team’s next step.

## 💡 Variations / Follow-ups

* Combine with **Mikado Method** (if an undone step breaks something, indent it and keep going).
* Use it in **multi-stages refactors**: TODO.md becomes the visible map of advancement.
* Integrate your **commit messages convention**: discuss with the team how they do this.
* Some teams prefer using a **shared Markdown pad** for remote ensembles (e.g. a shared Google Doc).

## 🪶 References

An **Indented TODO List** is a *lightweight practice* inspired by the Mikado Method and mindful programming:

* [A Slow Code Retreat to Be Less in a Hurry – Philippe Bourgau](https://philippe.bourgau.net/a-slow-code-retreat-to-be-less-in-a-hurry/)
* [code-in-flow/mindful-programming - rroblak](https://github.com/code-in-flow/mindful-programming)
* [Mikado Method — Ola Ellnestam & Daniel Brolund](https://mikadomethod.info/)