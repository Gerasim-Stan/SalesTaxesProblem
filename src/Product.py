import re
from src.Taxes import Taxes


class Product:
    """Defines methods for input and computation of product's final price"""

    def __init__(self, textInput):
        """Splits the input to groups with regex.
           No demands about input check were disposed,
           so none are implemented.
        """
        textCheckPattern = "(\d+)\s((imported\s)?\w+(\s\w+)*)\sat\s(\d+\.\d+)"
        match = re.search(textCheckPattern, textInput)
        self.count = match.group(1)
        self.product = match.group(2)
        self.price = float(match.group(5))

    def taxComputation(self):
        """Estimates taxes over the product's price and rounds the result"""
        price = round(self.price * Taxes().taxesSum(self.product), 2)
        roundedPrice = price % 0.05
        if roundedPrice == 0:
            return price
        else:
            return price + 0.05 - roundedPrice

    def finalPrice(self):
        """Estimates shelf price for the product"""
        return round(self.price + self.taxComputation(), 2)

    def saleOutput(self):
        """Formats output for receipt"""
        return str("%s %s: %.2f" % (self.count, self.product,
                                    self.finalPrice()))
