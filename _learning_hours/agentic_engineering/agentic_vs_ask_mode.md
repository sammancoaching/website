---
theme: agentic_engineering
name: agentic_vs_ask_mode
title: Agentic vs Ask Mode
kata: WarehouseDeskApp
difficulty: 1
author: larseckart
via: emilybache
tags:  agentic tdd
---

# {{ page.title}}

This is a first learning hour for people who have not yet fully understood the difference between agentic AI and the previous forms of AI that were available to them like "Ask mode" and autocomplete in the IDE.

## Learning Goals

* Describe how Agentic AI differs from AI "Ask mode" or autocomplete.
* Use an AI Agent to inspect, change and verify code via prompting.

## Session Outline

* 5 min connect: Give some examples of what you have already used AI for?
* 5 min concept: The Agent Loop
* 10 min demo: Using an AI Agent to refactor
* 30 min concrete practice: Use an AI Agent
* 5 min conclusion: Explain the main idea

## Connect - Give some examples of what you have already used AI for?
Pose an open question and ask people to write notes with their answers. If you don't understand something they write, ask them to explain verbally. There are no wrong answers or right answers you are looking for, you are connecting to what they already know. This is not supposed to be a long discussion or analysis: acknowledge their experiences and move on.

## Concept - The Agent Loop
Show the relationship diagram and explain it:

![agent loop.png](/assets/images/agent%20loop.png)

The numbers indicate the order that things happen in.

## Demo - Using an AI Agent to refactor
Open a small project like [WarehouseDeskApp](https://github.com/LarsEckart/harness-engineering-kata.git) that has some poorly written code that could be improved by refactoring. Show how to prompt the agent to achieve that. 

Show them the AI settings so that it will use an Agent Loop that includes compiling and/or linting. Keep it to the bare minimum of choices so the tool details don't overwhelm them. For example, use the 'auto' LLM selection. 

Show the normal workflow you recommend, which probably means asking it to improve the design in a specific way, inspecting changes, and using the AI to generate a commit message. The focus should be on the Agent loop and how it can check for itself whether it is making progress with the task you have set.

## Concrete Practice - Use an AI agent
Split into pairs and give them the same code that you showed in the demo, with the same AI tooling already set up. Ask them to do similar design improvement tasks using the Agentic setup. Go round and help if anyone gets stuck and answer questions - try to get every pair to the point where the agent has made acceptable code changes without manual intervention, and they were prepared to commit the results.

## Conclusions
Ask people to [explain the main idea]({% link _activities/conclusions/explain_main_idea.md %}) with a question similar to this:

* What can Agent mode do that Ask mode cannot?
