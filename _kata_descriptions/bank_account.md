---
title: Bank Account - 银行账户
kata_name: bank_account
---
# 银行账户

编写一个名为BankAccount的类，实现以下公共接口。

    public interface BankAccount
    {
        void deposit(int amount)
        void withdraw(int amount)
        void printStatement()
    }

(注意你可以用任何编程语言做这个练习，根据情况翻译上述代码)

## 语句示例
当你调用'printStatement'方法时，会在标准输出上打印出类似下面的内容。

    日期  ||  金额  ||  余额
    2012-01-14 || -500 || 2500
    2012-01-13 || 2000 || 3000
    2012-01-10 || 1000 || 1000

这个示例语句显示了2012年1月14日的一笔取款，以及1月13日和10日的两笔存款。

## 注意
* 你不能改变BankAccount的公共接口。
* 我们用 int 来表示钱，一般来说，这可能不是最好的主意。在一个真实的系统中，我们总是会使用一个可以保证任意精度的数据类型，但是在这里这样做会分散我们对练习的主要目的的注意力。
* 不要担心与银行对账单的准确格式相匹配，重要的是要打印一个有列标题的表格，并按日期排列交易。

### 鸣谢
这个卡塔是由 [Codurance](https://katalyst.codurance.com/bank)发明的。
