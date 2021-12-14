---
title: RPG Combat
kata_name: rpg_combat
---

# RPG Combat

This Kata that has you building simple combat rules as for a role-playing game (RPG). The domain doesn't include a map or any other character skills apart from their ability to damage and heal one another.

The problem is broken down into several user stories to help you to focus on doing one thing at a time. Complete one user story before starting on the next one. Be sure to work on the problem in small steps and pay close attention to the design of both the code and the automated tests in every step.

## Damage and Health

1. All Characters, when created, have:
    - Health, starting at 1000
    - May be Alive or Dead, starting Alive

1. Characters can Deal Damage to Characters.
    - Damage is subtracted from Health
    - When damage received exceeds current Health, Health becomes 0 and the character dies

1. A Character can Heal themselves.
    - Dead characters cannot heal

## Levels

1. All characters have a Level, starting at 1
   - A Character cannot have a health above 1000 until they reach level 5, when the maximum increases to 1500
   - A Character cannot Deal Damage to itself, even after they reach level 5

1. When dealing damage:
    - If the target is 5 or more Levels above the attacker, Damage is reduced by 50%
    - If the target is 5 or more Levels below the attacker, Damage is increased by 50%

## Factions

1. Characters may belong to one or more Factions.
    - Newly created Characters belong to no Faction.

1. A Character may Join or Leave one or more Factions.

1. Players belonging to the same Faction are considered Allies.
    - Allies cannot Deal Damage to one another.
    - Allies can Heal one another and non-allies cannot.

## Magical objects

1. As well as Characters there are also Magical Objects
   - Magical Objects have Health
   - The maximum amount of Health is fixed at the time the object is created
   - When reduced to 0 Health, Magical Objects are *Destroyed*
   - Magical Objects cannot be Healed by Characters
   - Magical Objects do not belong to Factions; they are neutral
    
1. Characters can gain health from a Healing Magical Object.
    - Characters can gain any amount of health from the Object, up to its maximum and theirs
    - Healing Magical Objects cannot deal Damage
    
1. Characters can deal Damage by using a Magical Weapon.
    - These Magical Objects deal a fixed amount of damage when they are used
    - The amount of damage is fixed at the time the weapon is created
    - Every time the weapon is used, the Health is reduced by 1
    - Magical Weapons cannot give Health to a Character

## Changing level

1. Level 1 Characters that survive 1000 damage points gain a level, (this may be counted over several battles)
   - a character cannot gain a level while receiving damage, it happens directly afterwards (if the player is still alive)
   - Level 2 Characters need to survive an additional 2000 damage points to gain a level, Level 3 Characters need to survive an additional 3000, and so on.
   
1. Level 1 Characters that have ever been part of 3 distinct factions gain a level
   - Level 2 Characters need to join an additional 3 distinct factions to gain a level, Level 3 Characters need to join an additional 3, and so on.

1. The maximum Level for Characters is 10
   - Characters cannot lose a level they have gained


## Acknowledgements

This Kata was invented by Daniel Ojeda Loisel and this description is adapted from [Steve Smith's version](https://github.com/ardalis/kata-catalog/blob/main/katas/RPG%20Combat.md)