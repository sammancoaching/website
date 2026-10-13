---
title: Binary Diagnostic
kata_name: binary_diagnostic
---

# Binary Diagnostic

You are given a diagnostic report consisting of a list of binary numbers. Calculate the power consumption of the submarine, which is: gamma rate × epsilon rate.

Both rates are derived from the report by looking at each column (bit position) across all numbers:

- **Gamma rate**: for each column, take the most common bit (0 or 1).
- **Epsilon rate**: for each column, take the least common bit.

For example, given this diagnostic report:

```
00100
11110
10110
10111
10101
01111
00110
```

The first column has bits `0,1,1,1,1,0,0`. `1` appears more often (4 times) than `0` (3 times), so the first bit of gamma is `1`. Across all five columns the most common bits are `1,0,1,1,0`, so gamma is `10110` (binary) = `22` (decimal).

Epsilon uses the least common bit in each column: `01001` (binary) = `9` (decimal).

Therefore power consumption = `22 × 9 = 198`.

### Acknowledgments

This kata is [Advent of Code 2021 Day 3](https://adventofcode.com/2021/day/3).
