# Ensemble retro, 20 November 2026

Session: Emily and Willem with Claude (following the Live Notes meeting), working on `_docs/calendar_events_plan.md`. Read this first at the start of the next session.

## Where we left off

- Committed (not pushed): `377c0f9` Phase 1, open space off addcal; `ccc4dff` Phase 2, ensemble off addcal (committed before the review was finished).
- Uncommitted, for review: learning hour on Wed 20 January 2027 17:00–18:30 Berlin; add-to-calendar buttons moved onto the event details pages (`_includes/add_to_calendar.html`), with the separate calendar pages removed; smaller buttons. A draft skill is at `.claude/skills/ensemble-session/SKILL.md`.
- To check: `next_ensemble` says the ensemble is on Fridays at 16:00, but addcal and `ensemble.md` say 15:00 Berlin.

## Timeline (UTC)

| Time | What happened |
|---|---|
| 13:57 | Found the lost to-do: `_docs/calendar_events_plan.md` (replace addcal) |
| 14:05 | Executive summary of the plan |
| 14:07–14:16 | Phase 1 built in one go: plugin, event page, `.ics`, tests (20/20) |
| 14:21–14:36 | Review on localhost: about 15 layout and wording changes |
| 14:41 | Commit `377c0f9` (Phase 1) |
| 14:42–14:47 | Phase 2 (ensemble) + repeat-rule fix, commit `ccc4dff` (too early) |
| 14:49–14:52 | Learning hour on 20 January; buttons moved onto the details pages |
| 14:52 | Retro |

## Tokens per step

From the Claude Code session log (`~/.claude/projects/<project>/<session-id>.jsonl`, which has `usage` on each model call):

| Step (UTC) | Model calls | Output | Input (new + cache write) | Cache read |
|---|---|---|---|---|
| 13:50 Joining + finding the plan | 22 | 7,704 | 53,379 | 1,606,116 |
| 14:05 Executive summary | 11 | 2,958 | 9,110 | 1,012,547 |
| 14:07 Phase 1 build | 47 | 27,402 | 59,954 | 6,162,818 |
| 14:21 Review on localhost | 168 | 66,869 | 142,072 | 38,206,464 |
| 14:41 Commit Phase 1 | 9 | 3,461 | 5,986 | 2,700,582 |
| 14:42 Phase 2 ensemble | 52 | 21,123 | 44,369 | 17,122,145 |
| 14:48 Learning hour + merge buttons | 33 | 11,340 | 23,893 | 11,880,138 |
| 14:52 Retro | 54 | 28,226 | 62,261 | 22,153,490 |
| **Total** | 396 | 169,083 | 401,024 | 100,844,300 |

- The review on localhost was the most expensive step (about 40%). Each spoken line woke the agent up for a read receipt or a page update.
- The Phase 1 build itself was cheap.
- Cache reads dominate: each call re-reads the whole growing session, so lines late in a long session cost more.

## Biggest problem

The first step was too big, and we couldn't follow what was going on while it ran. Claude built a whole plan phase (plugin, layout, pages, tests) in one go before there was anything to look at.

## What we'd like to do differently next time

1. **Ask big or small first.** At the start, Claude asks whether today is a big change or a small one.
2. **Work in small steps.** One small, visible, reviewable change at a time, with the team steering between steps, so we stay in the loop.
3. **Use a sub-agent for big work.** The plan is carried out by a sub-agent in the background, so the agent in the meeting stays free to answer and show what's happening.
4. **Mockups first for UI work.** 2–3 clickable variants before changing the real Jekyll pages. Most of this session went on layout changes to a real page.
5. **Set up the agent page from the start.** Main page with the newest answers at the top, plus `plan`, `decisions` and `retro` sub-pages, created unasked. Answers go on the page, not in chat.
6. **Commit only on "commit".** "Are we ready to commit?" is a question, not a go-ahead.
7. **Reset the agent session after a big chunk of work.** Commit, then start fresh with the plan and the meeting page as the handover.
8. **Keep the terminal readable.** Meeting traffic and diffs filled the Claude Code window. With a sub-agent doing the build and a one-line "what changed" note per step, the work is easier to follow.
9. **Fix the test/server clash.** `./build_and_test` stops a running `jekyll serve`. Build the tests into a separate folder, e.g. `_site_test`.
10. **Track tokens per step.** Ask the agent to sum the `usage` in the session log per timeline step at the end of the session. To save tokens: let the follower batch the meeting lines, and reset the session after big chunks.
11. **Make it a skill.** The `ensemble-session` skill covers points 1–6. Review the draft first thing next session.

## What went well

- Finding a half-forgotten plan took seconds, and the plan itself held up.
- Every change came with tests. Checking the time zones across the daylight saving changes confirmed that the Berlin times convert correctly.
- Feedback on the real page was fast, and changes landed within a minute or two.
- A real bug was found on the way: repeating events would have been exported from the next date, so the series would have moved later each week.
