SalesTaxesProblem
=================

This project implements the "Sales Taxes" problem:
---
Basic sales tax is applicable at a rate of 10% on all goods, except books,
food, and medical products that are exempt. Import duty is an additional
sales tax applicable on all imported goods at a rate of 5%, with no
exemptions.
When I purchase items I receive a receipt which lists the name of all the
items and their price (including tax), finishing with the total cost of the
items, and the total amounts of sales taxes paid. The rounding rules for
sales tax are that for a tax rate of n%, a shelf price of p contains (np/100
rounded up to the nearest 0.05) amount of sales tax.
Write an application that prints out the receipt details.

--
Class Taxes defines methods for estimation of taxes. There are three static methods that don't need instantiated object to be used, and also a method that calculates the amount of taxes that should be accounted. Notice the list with products exempt from basic sale tax.

Class Product evaluates the input and formats output for receipt of one product.

Class Products formats print output for receipt.

Project Dependencies
--------------------
* [Python 3](https://www.python.org/) *(or later)*

License
-------
The project falls under [GNU General Public License *(version 3)*](http://choosealicense.com/licenses/gpl-3.0/)

[License to use Python](https://docs.python.org/3/license.html#terms-and-conditions-for-accessing-or-otherwise-using-python)
