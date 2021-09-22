---
title: Parse Command-Line Args
kata_name: parse_args
---

# Parse Command-Line Args

Given your program is called like this:

    your_app --log log.txt --verbose 3 --script ascript.scr --debug true --format JSON

Write a function that can parse those arguments into a nice datastructure that will be easy for your program to use all the values afterwards, with the correct types. You will also need some way to specify what argument names and types you are expecting. For the example above you might specify something like this in json:

    {
        "log": str, 
        "verbose": int,
        "script": str,
        "debug": bool,
        "format": str,
    }

Note: feel free to specify this in another way if your language isn't good at parsing json.

You should also have some error handling, for example for if unexpected arguments are given, or if the flags are spelled incorrectly.

There are very good libraries available that do this kind of argument parsing already. Doing it yourself will give you a better understanding of what those libraries are doing for you. Mostly it's just for the exercise of building something using TDD though. TDD is fun!
