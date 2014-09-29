class Taxes:
    """Defines methods for taxes calculation"""
    EXEMPT_LIST = ["book", "chocolate bar", "box of chocolates",
                   "packet of headache pills"]

    @staticmethod
    def taxesPooling(product):
        """Checks, and eventually adds in list, taxes
           that should be accounted.
        """
        taxes = []
        if Taxes.productExempt(product):
            taxes.append(0.1)
        if Taxes.productImported(product):
            taxes.append(0.05)
        return taxes

    @staticmethod
    def productExempt(product):
        """Checks if the product is in the list of products,
           exempt from taxes.
        """
        productName = product.replace("%s " % "imported", "")
        return productName not in Taxes.EXEMPT_LIST

    @staticmethod
    def productImported(product):
        """Checks if the product is imported"""
        return "imported" in product

    def taxesSum(self, product):
        """Calculates all taxes that should be accounted"""
        taxes = Taxes.taxesPooling(product)
        taxesCost = 0
        for tax in taxes:
            taxesCost += tax
        return taxesCost
