from src.Product import Product
from src.Products import Products
import unittest


class TestProduct(unittest.TestCase):
    """These tests are picked from the sample inputs and outputs,
       given in "Problem 2"'s definition.
    """

    def setUp(self):
        product1 = Product("1 book at 12.49")
        product2 = Product("1 music CD at 14.99")
        product3 = Product("1 chocolate bar at 0.85")
        self.scenario1_products = Products([product1, product2, product3])

        product4 = Product("1 imported box of chocolates at 10.00")
        product5 = Product("1 imported bottle of perfume at 47.50")
        self.scenario2_products = Products([product4, product5])

        product6 = Product("1 imported bottle of perfume at 27.99")
        product7 = Product("1 bottle of perfume at 18.99")
        product8 = Product("1 packet of headache pills at 9.75")
        product9 = Product("1 box of imported chocolates at 11.25")
        self.scenario3_products = Products(
            [product6, product7, product8, product9])

    def test_scenario_1_tax(self):
        self.assertEqual(self.scenario1_products.taxesSum(),
                         "Sales Taxes: " + "1.50")

    def test_scenario_1_result(self):
        self.assertEqual(self.scenario1_products.result(),
                         "Total: " + "29.83")

    def test_scenario_2_tax(self):
        self.assertEqual(self.scenario2_products.taxesSum(),
                         "Sales Taxes: " + "7.65")

    def test_scenario_2_result(self):
        self.assertEqual(self.scenario2_products.result(),
                         "Total: " + "65.15")

    def test_scenario_3_tax(self):
        self.assertEqual(self.scenario3_products.taxesSum(),
                         "Sales Taxes: " + "6.70")

    def test_scenario_3_result(self):
        self.assertEqual(self.scenario3_products.result(),
                         "Total: " + "74.68")


if __name__ == '__main__':
    unittest.main()
