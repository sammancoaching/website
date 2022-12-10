---
title: Filename Range - 文件名范围
kata_name: filename_range
---

当你在[cyber-dojo](https://cyber-dojo.org/)中重命名一个文件时，它试图提供帮助，只选择它认为你要改变的文件名的一部分。

你的任务是编写一个函数，给定一个字符串文件名，并返回一对整数，指定所选范围的开始和结束索引（在文件名中）。

## 规则和例子
首先，它假设你想保留扩展名。

    "hiker.cpp" ==> "hiker" 被选中。
    "diamond.h" ==> "diamond" 被选中。

第二，如果文件名包括 "test"、"test"、"spec"或
"step"（不区分大小写），它假定你也想保留这些。
以及任何 "分隔符"（点、下划线、连字符）。

    "HikerTest.js" ==> "Hiker "被选中。
    "Diamond_Spec.feature" => "Diamond" 被选中。
    "fizz.buzz-test.js" => "fizz.buzz "被选中。

第三，如果文件名是在dir/
假定你也想保持那样。

    "test/FizzBuzz_test.exs" => "FizzBuzz" 被选中。
    "src/test/Roman.spec.re" => "Roman" 被选中。

下面是一个JSON数据结构，你可以在你的测试中使用。

    {
    "src/Hiker_spec.re"。[4,9],
    "test/hiker_test.exs": [5,10],
    "wibble/test/hiker_spec.rb"。[12,17],
    "hiker_steps.rb"。[0,5],
    "hiker_spec.rb": [0,5],
    "test_hiker.rb": [5,10],
    "test_hiker.py": [5,10],
    "test_hiker.sh": [5,10],
    "test_hiker.sh": [6,11],
    "test_hiker.coffee": [5,10],
    "hiker_spec.coffee": [0,5],
    "hikerTest.chpl"。[0,5],
    "hiker.test.c"。[0,5],
    "hiker_tests.c"。[0,5],
    "hiker_test.c": [0,5],
    "hiker_Test.c": [0,5],
    "HikerTests.cpp": [0,5],
    "hikerTests.cpp": [0,5],
    "HikerTest.cs": [0,5],
    "HikerTest.java": [0,5],
    "DiamondTest.kt"。[0,7],
    "HikerTest.php": [0,5],
    "hikerTest.js": [0,5],
    "hiker-test.js": [0,5],
    "hiker-spec.js": [0,5],
    "hiker.test.js": [0,5],
    "hiker.test.ts": [0,5],
    "hiker_tests.erl": [0,5],
    "hiker_test.clj": [0,5],
    "fizzBuzz_test.d": [0,8],
    "hiker_test.go": [0,5],
    "hiker.test.R": [0,5],
    "hikertests.swift": [0,5],
    "HikerSpec.groovy"。[0,5],
    "hikerSpec.feature"。[0,5],
    "hiker.feature": [0,5],
    "hiker.fun": [0,5],
    "hiker.t": [0,5],
    "hiker.plt": [0,5],
    "hiker": [0,5],
    };


## 鸣谢
此 Kata 在[cyber-dojo](https://cyber-dojo.org/)上有描述。