# Ensemble retro, 27 November 2026

Session: Emily and Willem with Claude (following the Live Notes meeting). **Small session**, steered one task at a time. Read this, and `ensemble_retro_2026-11-20.md`, at the start of the next session.

## Where we left off
- Committed (not pushed; Emily pushes): `cee729d`, `1b089b2`, `e7e6132`, `63c96e0`.
- **Uncommitted, review first next session:** #9 B (tests build into `_site_test`: `tests/built_site.py`, 7 test files, `conftest.py`, `build_and_test(.cmd)`, `_config.yml` exclude, `.gitignore`); `ensemble-session` skill §5 (token table); this retro doc. A full `./build_and_test` was green with the dev server up.

## Timeline (UTC)
| Time | What happened |
|---|---|
| 13:52 | Checked last retro's 11 action items: most are in the skill; #9 and #11 open |
| 13:57 | Emily: small session, steered one by one |
| 14:05 | Willem: calendar links should open a new tab → 4-line fix, reviewed via the diff on the page, committed `cee729d` |
| 14:08 | Second learning hour (17 Feb): options A/B → B, a `dates:` list (plugin + tests by a sub-agent) |
| 14:13 | "Following events" line; found that Google & co. take one date per link |
| 14:15 | 3 HTML mockups → B; built; "which buttons are for which date?" → realistic mockups with the site's CSS (6 variants) |
| 14:21 | Willem: "wall clock" is Claude-speak → renamed to `local` |
| 14:22 | Variant 3 on the real page (a box per date, headings kept) |
| 14:25 | "Will the tests break after 20 Jan?" → yes → Ruby unit tests with a fixed "now" and Willem's heredoc fixtures (sub-agent) |
| 14:31 | Dropped 6 date-dependent Python tests |
| 14:36 | "Add series to calendar" for repeating events |
| 14:39 | All one-off events moved to `dates:` (**before** the team confirmed) → full test run green (Ruby 18, pytest 22) |
| 14:42 | Committed `1b089b2` (feature) + `e7e6132` (tests) |
| 14:46 | #9: why does `conftest.py` kill all Ruby? Option A (kill only the test server) tested → committed `63c96e0` |
| 14:49 | #9 option B started (own `_site_test` folder) in a sub-agent |
| 14:50 | Retro |
| 14:53 | #9 B done (sub-agent): full test run green with the dev server still up |

## What went well
- **Small steps worked.** Each change was small enough to review on the page within a minute.
- **Answers and diffs on the page:** Willem: "we didn't have to open our editor to do the review".
- **Mockups first** stopped us from building the wrong layout twice. The second round used the site's real stylesheet, which made them believable.
- **Sub-agents** took the bigger chunks (plugin, Ruby tests, #9 B), and the meeting page stayed responsive.
- Willem: "a lot faster than doing it by hand, especially now that we have unit tests, which we didn't have before at all".
- Good questions from the team led to real fixes: unit tests instead of tests that depend on real dates; why `taskkill` was there (git archaeology gave the answer in seconds).
- Retro actions 1–6 from last time all held up. Willem: "a lot easier to follow than last time": the tabs, plan, decisions and Kaizen board were all there unasked.

- **Conversational refactoring** (Willem): Claude refactored while we talked about the code (the `local` rename), we were happy with the changes, and the code got more readable. Emily: "a code review where we talk about the code and it goes away and implements what we ask". Willem: "the kind of code review you'd always want: a conversation, with changes as you go. So that's to pull requests."
- It felt more responsive than last time (Emily, Willem): sub-agents kept the meeting agent free.

## What didn't go so well
- **Claude acted before the team confirmed** the "same format for all events" change, just as Willem said "commit first". It ended up in the same commit run.
- **The dev server broke 5 times:** the test run killed it twice, and the Sass compiler died 3 times (`end of file reached`, after two rebuilds at once). Each time it needed a restart.
- **Naming:** "wall clock" and `wall_start` read as robot-speak until renamed. (Willem: that code was already there from last time.)
- **"Should we ask it to commit?" / "Yeah"** was taken as "commit". Probably right, but a borderline call.
- **Work kept going during the retro** (#9 B, the retro doc, the skill tweak), so we ended with uncommitted changes to review next time.
- The `.ics` file couldn't be opened on this machine, so checking the result meant pasting the file onto the page.

## Tokens per step
From the session logs (main + 3 sub-agents, `usage` per model call):

| Step (UTC) | Duration | Calls | Output | Input (new + cache write) | Cache read |
|---|---|---|---|---|---|
| 13:50 Joining, pages, retro check | 7 min | 17 | 4,894 | 50,125 | 1,157,019 |
| 13:57 Small session; waiting | 8 min | 33 | 1,210 | 14,047 | 2,958,523 |
| 14:05 New-tab links + commit | 3 min | 43 | 7,160 | 33,822 | 4,905,997 |
| 14:08 Second learning hour: options, plugin (sub-agent) | 5 min | 55 | 12,156 | 88,383 | 7,267,125 |
| 14:13 Following-events line, Google caveat, diff | 2 min | 18 | 6,627 | 22,401 | 3,084,851 |
| 14:15 Mockups, B built, grouping mockups | 5 min | 46 | 13,256 | 42,300 | 9,296,971 |
| 14:20 Rename wall-clock, variant 3, Sass restarts | 5 min | 25 | 9,391 | 26,047 | 5,965,549 |
| 14:25 Test questions, Ruby unit tests (sub-agent) | 6 min | 36 | 16,697 | 84,195 | 7,352,526 |
| 14:31 Remove Python tests, hover, ensemble heading | 6 min | 28 | 8,839 | 25,185 | 8,133,736 |
| 14:37 Commit question, all events to dates, full test run | 5 min | 22 | 9,978 | 21,831 | 6,931,362 |
| 14:42 Commit; #9 options | 4 min | 17 | 5,600 | 13,465 | 5,662,691 |
| 14:46 #9 A + test + commit; B (sub-agent) | 4 min | 9 | 4,069 | 8,351 | 3,097,388 |
| **Total (to 14:50)** | 60 min | 349 | 99,877 | 430,152 | 65,813,738 |

- 13:57–14:05 cost **33 calls doing nothing**: every spoken line woke the agent, which replied "Following the meeting." That's the price of following every line.
- The sub-agent steps (14:08, 14:25) cost the most input, but they kept the meeting agent quick.
- Keeping the mics on vs. muting made no difference to tokens; muting was just annoying (Emily, Willem). Today's fixes were simpler than last week's calendar work, so the comparison is only a hint (Willem).
- **Compared with last time** (20 Nov, 62 min): 396 → 349 calls, output 169k → 100k, cache reads 101M → 66M. That's about a third less, for more work done (4 commits + #9 B, with tests).
- Cache reads dominate, as last time (67M), and grow as the session gets longer.

## Willem's notes
- "The space is defined by the patterns that keep happening there" (Christopher Alexander). We keep saying "please build and test".
- **Could a pre-commit hook run the build and test?** Then "commit" includes the test run without anyone having to remember. Needs #9 B first, so the hook doesn't break the server.

## Try next time
0. **Review the `ensemble-session` skill first thing** (Willem). It's carried over from last time (#11). It worked well in use; check whether it can be shorter and more hand-written (Willem: hand-written skills seem to work better). Update section 4: `build_and_test` no longer stops the dev server (#9).
1. **Wait for an explicit "go" on changes the team is still discussing.** "I'd like…" is input, not a go-ahead.
2. **Finish #9 B** (own `_site_test` folder, exclude test artifacts from the watcher), so tests and the server never clash, and the Sass error goes away.
3. **Kaizen and feature backlogs kept separate** (Rob's idea, via Willem). It worked on the plan page; keep it.
4. **Mockups with the real site CSS** from the start.
5. **Reset the session** after a big chunk (still not done: this session ran the whole meeting).
6. **Name things in domain words** (local time, not wall clock); review names in the diff.
7. **Pre-commit hook running `./build_and_test`** (Willem), once #9 B is in.
8. Open: remove the ensemble Python tests (they break in April 2027)? Add a test that the page renders its per-date buttons?

## How the token numbers were made
Sum `message.usage` per assistant message (deduplicated by `message.id`) in the session log `~/.claude/projects/<project>/<session-id>.jsonl` plus `<session-id>/subagents/*.jsonl`, bucketed by `timestamp` into the timeline steps. Columns: calls, `output_tokens`, `input_tokens + cache_creation_input_tokens`, `cache_read_input_tokens`.
