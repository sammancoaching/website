---
title: Office Cleaning Robot
kata_name: office_cleaner
---

# Office Cleaning Robot

Implement a RobotCleaner which can clean the office at night. The robot receives instructions about where to move and clean, and at the end reports how much of the office it has cleaned.

### Input
* Input is given to standard input.
* First input line: a single integer that represents the number of commands the robot should expect to execute before it knows it is done. The number will be in the range between 0 and 10,000.
* Second input line: consists of two integer numbers that represents the starting x y coordinates of the robot. The value of each coordinate will be in the range between -100,000 and +100,000.
* The third, and any subsequent line, will consist of two pieces of data. The first will be a single uppercase character that represents the direction on the compass the robot should head (E, W, S, N). The second will be an integer representing the number of steps, between 0 and 100,000, that the robot should take in said direction.
* All input should be considered well-formed and syntactically correct. There is no need, therefore, to implement elaborate input parsing.
* The robot will never be sent outside the bounds of the plane.
* There will no leading or trailing white space on any line of input.
* Any multi-valued line of input will have a single white space character between each
  value.

### Output
The output of your program should be a number u, which represents the number of unique places in the office that were cleaned. The output of the number u should be prefixed by "=> Cleaned: ".
* Output should be written to standard output.
* The only output should be the number of unique places that the robot cleaned.
  Please note that the robot cleans at every vertex it touches not just where it stops.
* There should be no leading or trailing whitespace on any line of output.

### Example
Sample input:

	2
	10 22
	E 2
	N 1

Sample output:

	=> Cleaned: 4

## Refactoring Kata
There are several implementations you can use to practice Refactorings.

## Acknowlegements
I learnt this exercise from Luca Minudel. It is quite similar to [Mars Rover]({% link _kata_descriptions/mars_rover.md %}).
