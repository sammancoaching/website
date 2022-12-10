---
title: Vending Machine
kata_name: vending_machine
---

Vending Machine Kata
====================

In this exercise you will build the brains of a vending machine.  It will accept money, make change, maintain
inventory, and dispense products.  All the things that you might expect a vending machine to accomplish. 
Features are detailed below.

Accept Coins
------------

The vending machine will accept valid coins (nickels, dimes, and quarters) and reject invalid ones (pennies). Coin values:

* Penny - 1 cent
* Nickel - 5 cents 
* Dime - 10 cents 
* Quarter - 25 cents

When a valid coin is inserted the amount of the coin will be added to the current amount and the display will be updated.
When there are no coins inserted, the machine displays INSERT COIN.  Rejected coins are placed in the coin return.

Select Product
--------------

There are three products: cola for $1.00, chips for $0.50, and candy for $0.65.  When the respective button is pressed
and enough money has been inserted, the product is dispensed and the machine displays THANK YOU for 5 seconds.  
After that, it will display INSERT COIN and the current amount will be set to $0.00.  If there is not enough money
inserted then the machine displays PRICE and the price of the item for 5 seconds. After that the display will show
either INSERT COIN or the current amount entered, as appropriate.

Make Change
----------- 

When a product is selected that costs less than the amount of money in the machine, then the remaining amount is placed
in the coin return.

Return Coins
------------

When the return coins button is pressed, the money the customer has placed in the machine is returned and the display 
shows INSERT COIN.

Sold Out
--------

When the item selected by the customer is out of stock, the machine displays SOLD OUT for 5 seconds.  After that,
it will display the amount of money remaining in the machine or INSERT COIN if there is no money in the machine.


Exact Change Only
-----------------

When the machine is not able to give change for any of the items that it sells, it will display EXACT CHANGE ONLY 
instead of INSERT COIN.

# Acknowledgments

This Kata is by Guy Royse and his version is available [here](https://github.com/guyroyse/vending-machine-kata)