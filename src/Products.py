class Products:
    """Defines methods for estimation and print of
       taxes and total price of group of products.
    """

    def __init__(self, products):
        self.products = products

    def taxesSum(self):
        """Estimates and prints the value of all accounted taxes"""
        tax = 0
        for product in self.products:
            tax += product.taxComputation()
        return str(("Sales Taxes: %.2f") % tax)

    def result(self):
        """Estimates and prints the sum of the shelf prices of all products"""
        resultSum = 0
        for product in self.products:
            resultSum += product.finalPrice()
        return str(("Total: %.2f") % resultSum)
