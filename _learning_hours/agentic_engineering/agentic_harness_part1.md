---
theme: agentic_engineering
name: harness_for_agentic_autonomy
title: Designing a Harness for Agentic Autonomy (Part 1)
kata: WarehouseDeskApp
difficulty: 1
author: martinsson
via: emilybache
tags:  agentic tdd
---

# Designing a Harness for Agentic Autonomy (Part 1)

Starting from no harness at all and a simple prompt to add a new feature, we learn what difference an agentic harness makes. The goal with a harness is for the agent to make autonomous decisions about code changes that align with the qualities you value. This learning hour was originally designed as a longer workshop, so it is split into several parts.  See also [Agentic Harness Part 2]({% link _learning_hours/agentic_engineering/agentic_harness_part2.md %}).

## Learning Goals

* Define the difference between a prompt and a harness
* Use an AGENTS.md file as a harness to ensure the coding agent creates unit tests as well as code.

## Session Outline

* 5 min connect: Discuss: In what ways can you influence the code produced by a coding agent?
* 5 min concept: What is a Prompt, what is an agent Context, what is an agent Harness
* 40 min concrete practice: Build a new feature with and without a Harness
* 5 min conclusion: Explain the main idea

### Connect
Ask: In what ways can you influence the code produced by a coding agent? Give me [Three Facts]({% link _activities/connect/three_facts.md %}). You are hoping for answers like - through the prompt, through the AGENTS.md file, through the documentation in the project, through documentation it can find on the internet.

### Concept
Even if they seem to understand all this from the Connect discussion, it's worth going over some basic terms.

* Prompt - the text you write in the "chat" window that specifies the current task the agent should work on
* Context - the full text the agent is currently working with which results in the output you see. Note the context also includes text you can't see - the system prompt.
* Harness - the metaphor is with the LLM being the horse and the work you want it to do is the cart. The harness is all the rules and context and tooling you put in place to help the horse to pull the cart in the right direction. 

A Harness might include:
* The AGENTS.md file
* The README.md file and other documentation in your repository
* Skills (other markdown files available to the agent)
* deterministic scripts, eg linters and compilers
* Architectural documents and constraints, eg [ArchUnit](https://www.archunit.org/) 

### Concrete
Introduce the exercise. The "WarehouseDesktopApp" manages inventory. The [starting code](https://github.com/martinsson/harness-engineering-kata) contains basic functionality and a description of a new desired feature in "feature.md". The code has a [Long Method]({% link _code_smells/long_function.md %}) code smell and there are no unit tests. The README file contains information about how to build the code and run the "Demo Day" application.

Note: Some people might have files in their user home folder that the agent will automatically load - we suggest disabling them for this exercise so you can see what the agent does without any harness.

#### Step 1: No Harness
Use this prompt:

```
Implement the feature from feature.md
```

If it can't work out how to build the code and run the Demo Day application, give it that information in the prompt too.

Review the quality of the code changes. Usually with this prompt, the agent implements the feature but does not create any unit tests or address the code smell. (If your agent does, try again with a less good/cheaper LLM!)

#### Step 2: Agent Instruction File
Revert the code. Create an AGENTS.md file in your repository and include this text: 

```
Add unit tests for new features
```

Start a new context window and give this prompt again:

```
Implement the feature from feature.md
```
    
Review the code changes. Hopefully, this time it will have created unit tests. Usually, it will not have fixed the code smell. (If your agent does, try again with a less good/cheaper LLM!) Discuss anything it did which doesn't align with your preferences for *test* design.

#### Step 3: Iterate to improve the Agent Instruction File
Update the AGENTS.md file with additional information about your preferences for test design. For example, you might want it to use a particular test framework or style of assertions. If it has only created tests for the new functionality, tell it to add regression tests for the rest of the code too. 

Repeat the process of reverting the code (while keeping your changes in the AGENTS.md file) and use a new context window with the same prompt every time until the code it writes has good enough tests.

At the end of the exercise, commit your code so you can resume with Part 2 in the next learning hour.

### Conclusions
Ask people to [explain the main idea]({% link _activities/conclusions/explain_main_idea.md %}) of an agentic Harness.
