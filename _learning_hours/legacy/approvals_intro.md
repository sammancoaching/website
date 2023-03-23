---
theme: legacy
title: Intro to Approvals
kata: fizzbuzz
difficulty: 1
author: nitsanavni
updated: 2023-03-23
---

# Intro to Approvals

This learning hour is also published [here on GitHub](https://github.com/nitsanavni/intro-to-approvals-learning-hour/blob/main/description.md), which may be a more up-to-date version of it.

You can find an implementation of this learning hour [here](https://github.com/nitsanavni/intro-to-approvals-learning-hour/blob/main/frames/index.md).

For remote sessions I recommend a shared [gitpod](https://www.gitpod.io/docs/introduction) workspace, and work directly from the markdown files.

## Audience

-   Learners are familiar with unit testing
-   Preferably, familiar with TDD
-   No knowledge of Approvals is needed

## Goals

-   Learners to be familiar with Approval Tests
-   Learners to experience the contrast with micro-assertions

In this Learning Hour, we focus on building simple code from scratch only.

## Agenda

-   Connect - 5m
-   Concept - explain + demo - 15m
-   Concrete - 30m (10m + 15m)
-   Conclusion - 5m

(My first attempt took 1h 17m.)

## Connect

Ask -

> How do you usually **structure** tests?
>
> How is a single test structured?
>
> How are multiple tests structured for a single module?

## Concept - Approval Tests Intro Explanation

See this [explanation frame](https://github.com/nitsanavni/intro-to-approvals-learning-hour/blob/main/frames/explain.md).

## Concept - Demo

Demo: build the same code twice

1. The first time - with micro asserts
2. The second time - using approvals

I chose [FizzBuzz]({% link _kata_descriptions/fizzbuzz.md %}) as the kata, with a starting position from the [intro to approvals learning hour](https://github.com/nitsanavni/intro-to-approvals-learning-hour) git repo.

## Concrete #1 - Build with Micro-Asserts

Prepare a starting position of the kata - the same kata you used for the Demo.

Provide clear, step-by-step instructions - a checklist. (I learned this method from [Llewellyn Falco]({% link society/contributors/isidore.md %}))

If learners are familiar with ensemble work, have them rotate after each completed step.

Emphasize that they should take their time, no need to complete all steps.

Stop and go to the next exercise when they get the point.

Example snippet of such a checklist:

> -   [ ] `fizzbuzz(3)` (Fizz)
      >
      >     -   [ ] add a new test / or new assert
>     -   [ ] see it fail
>     -   [ ] make it pass, with the smallest change possible
>     -   [ ] refactor if you like
>
> -   [ ] `fizzbuzz(4)` (just another number)
      >
      >     -   [ ] add a new test / or new assert
>     -   [ ] **challenge / optional:** see it fail
>     -   [ ] make it pass, with the smallest change possible
>     -   [ ] refactor if you like

The full checklist is [here](https://github.com/nitsanavni/intro-to-approvals-learning-hour/blob/main/frames/exercise-use-asserts.md).

## Concrete #2 - Build with Approvals

Same as previous exercise, now with approvals.

See example checklist [here](https://github.com/nitsanavni/intro-to-approvals-learning-hour/blob/main/frames/exercise-use-approvals.md).

## Conclusion

Ask -

> "how did that feel?"

And gather people's thoughts.