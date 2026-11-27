---
name: ensemble-session
description: Kick off and run a live ensemble (mob) session on this repo where Claude follows a Live Notes meeting and works for the whole team. Use at the start of an ensemble session, or when someone pastes a Live Notes meeting link and asks Claude to join as the team's agent. Triggers on "start an ensemble session", "join the ensemble", "kick off the session".
---

# Ensemble session

The team works on this repo together and steers Claude live. The aim is to keep the team in the loop: small steps, visible progress, the team deciding between steps.

## 1. Before any work: ask big or small

Ask once on the agent page (and wait for the answer):

> **Big or small today?** Small = a few page/style tweaks we steer one by one. Big = a plan phase or a new feature (run in a sub-agent, in reviewable steps).

## 2. Set up the agent page from the start

Do not wait to be asked. Create these right after joining:

- **Main page:** a `**Now:**` line, then `## Latest answer` with the newest answers at the top. Answer on the page, not in chat. People watch the page.
- **`plan` sub-page:** the plan, as a table of steps with their status.
- **`decisions` sub-page:** each decision, with who made it.
- **`retro` sub-page:** filled in at the end, when asked.

## 3. Work in small, visible steps

- One reviewable change per step, e.g. "plugin only, show the `.ics`", then "page only, show it". Do not do a whole plan phase in one go.
- **Big work goes to a background sub-agent**, so the meeting agent stays free to answer. After each step, post one short "what changed + where to look" line on the page.
- **UI work: mockups first.** Publish 2–3 clickable HTML variants as an artifact before touching Jekyll layouts.
- Before acting, say on the page what you understood ("Emily asked: … On it."), so the room can correct you.
- Thinking aloud is not a request. If you're unsure, ask in one line.

## 4. Repo specifics

- Keep `./build_and_run` (http://localhost:4000) running for the team. `./build_and_test` stops it, so restart it after every test run and say so on the page.
- Run `./build_and_test` after JavaScript, plugin or page add/remove changes (see AGENTS.md).
- **Commit only when someone says "commit".** "Are we ready to commit?" is a question: answer it (tests, what's unverified) and wait. Use the `commit-notation` skill. Never push unless asked.

## 5. End of session

When the team moves to retro: put a summary of what is uncommitted, committed and still open on the main page, and fill the `retro` sub-page with the timeline, what went well, what didn't and what to try next time. Add a tokens-per-step table (duration, calls, output, input, cache read), summed from the session log and its sub-agent logs, and compare it with the previous retro. Save the retro as `_docs/ensemble_retro_<date>.md` for the next session.
