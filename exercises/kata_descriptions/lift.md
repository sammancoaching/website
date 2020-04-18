---
layout: default
title: Lift
parent: Kata Descriptions
grand_parent: Exercises
nav_order: 3
---

# Lift

- a lift moves between a number of floors.
- a lift has a panel of buttons passengers can press to _request_ floors.
- people can call the lift from other floors. A _call_ has both a floor and a desired direction.
- a lift has doors which may be open or closed.
- a lift fulfills a _request_ when it moves to the requested floor and opens the doors.
- a lift fulfills a _call_ when it moves to the correct floor, is about to go in the called direction, and opens the doors.
- a lift can only move between floors if the doors are closed.

### Additional features
When you have a single lift working, you may want to tackle these further features: 

- there can be more than one lift.
- only one lift needs to respond to each call.
- on each floor there is a monitor above each lift door. While the lift is moving it shows which floor it is on.
- when the lift stops at a floor to answer a call, the monitor shows which direction it will go in.
- when fulfilling a call, the relevant lift makes a 'DING' as it opens the doors.

### Acknowledgements
This kata is described on [Kata-Log](https://kata-log.rocks/lift-kata) but I have changed it slightly
