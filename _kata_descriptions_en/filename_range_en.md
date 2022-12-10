---
title: Filename Range
kata_name: filename_range
---

When you rename a file in [cyber-dojo](https://cyber-dojo.org/), it tries to be helpful and selects only the part of the filename it thinks you will want to change.

Your task is to write a function that is given a string filename and which returns a pair of integers specifying the start and end indexes (into the filename) of the selected range.

## Rules and Examples
First, it assumes you will want to keep the extension:

    "hiker.cpp" ==> "hiker" is selected.
    "diamond.h" ==> "diamond" is selected.

Second, if the filename includes the word "tests", "test", "spec", or
"step" (case insensitive) it assumes you will want to keep those too,
together with any 'separator' characters (dot, underscore, hyphen).

    "HikerTest.js"  ==> "Hiker" is selected.
    "Diamond_Spec.feature" => "Diamond" is selected.
    "fizz.buzz-tests.js" => "fizz.buzz" is selected.

Third, if the filename is in a dir/
it assumes you will also want to keep that.

    "test/FizzBuzz_test.exs" => "FizzBuzz" is selected.
    "src/test/Roman.spec.re" => "Roman" is selected.

Here is a JSON data structure you can use in your tests.

    {
    "src/Hiker_spec.re": [4,9],
    "test/hiker_test.exs": [5,10],
    "wibble/test/hiker_spec.rb": [12,17],
    "hiker_steps.rb": [0,5],
    "hiker_spec.rb": [0,5],
    "test_hiker.rb": [5,10],
    "test_hiker.py": [5,10],
    "test_hiker.sh": [5,10],
    "tests_hiker.sh": [6,11],
    "test_hiker.coffee": [5,10],
    "hiker_spec.coffee": [0,5],
    "hikerTest.chpl": [0,5],
    "hiker.tests.c": [0,5],
    "hiker_tests.c": [0,5],
    "hiker_test.c": [0,5],
    "hiker_Test.c": [0,5],
    "HikerTests.cpp": [0,5],
    "hikerTests.cpp": [0,5],
    "HikerTest.cs": [0,5],
    "HikerTest.java": [0,5],
    "DiamondTest.kt": [0,7],
    "HikerTest.php": [0,5],
    "hikerTest.js": [0,5],
    "hiker-test.js": [0,5],
    "hiker-spec.js": [0,5],
    "hiker.test.js": [0,5],
    "hiker.tests.ts": [0,5],
    "hiker_tests.erl": [0,5],
    "hiker_test.clj": [0,5],
    "fizzBuzz_test.d": [0,8],
    "hiker_test.go": [0,5],
    "hiker.tests.R": [0,5],
    "hikertests.swift": [0,5],
    "HikerSpec.groovy": [0,5],
    "hikerSpec.feature": [0,5],
    "hiker.feature": [0,5],
    "hiker.fun": [0,5],
    "hiker.t": [0,5],
    "hiker.plt": [0,5],
    "hiker": [0,5],
    };

     
## Acknowledgements
This kata is described on [cyber-dojo](https://cyber-dojo.org/).