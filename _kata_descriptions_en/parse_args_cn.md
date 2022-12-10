---
title: Parse Command-Line Args
kata_name: parse_args
---

# 解析命令行参数

鉴于你的程序是这样调用的：

    your_app --log log.txt --verbose 3 --script ascript.scr --debug true --format JSON

编写一个函数，可以将这些参数解析成一个漂亮的数据结构，这样可以方便你的程序事后使用所有的值，而且类型正确。你还需要一些方法来指定你所期望的参数名称和类型。对于上面的例子，你可以在json中指定类似这样的东西。

    {
        "log": str, 
        "verbose": int,
        "script": str,
        "debug": bool,
        "格式": str,
    }

注意：如果你的语言不善于解析json，请随意以其他方式指定。

你还应该有一些错误处理，例如，如果给出了意想不到的参数，或者标志的拼写不正确。

现在已经有非常好的库可以做这种参数解析。自己动手会让你更好地了解这些库为你做了什么。不过大多数情况下，这只是为了练习使用TDD来构建一些东西。TDD是很有趣的!
