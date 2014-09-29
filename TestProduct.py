from src.Product import Product
import unittest


class TestProduct(unittest.TestCase):
    """These tests are derived from the sample inputs and outputs
       in "Problem 2"'s definition.
    """

    def test_book_sample(self):
        self.product = Product("1 book at 12.49")
        result = self.product.saleOutput()
        self.assertEqual(result, "1 book: 12.49")

    def test_musicCD_sample(self):
        self.product = Product("1 music CD at 14.99")
        result = self.product.saleOutput()
        self.assertEqual(result, "1 music CD: 16.49")

    def test_chocolate_bar_sample(self):
        self.product = Product("1 chocolate bar at 0.85")
        result = self.product.saleOutput()
        self.assertEqual(result, "1 chocolate bar: 0.85")

    def test_imported_box_of_chocolates_sample(self):
        self.product = Product("1 imported box of chocolates at 10.00")
        result = self.product.saleOutput()
        self.assertEqual(result, "1 imported box of chocolates: 10.50")

    def test_imported_bottle_of_perfume_sample1(self):
        self.product = Product("1 imported bottle of perfume at 47.50")
        result = self.product.saleOutput()
        self.assertEqual(result, "1 imported bottle of perfume: 54.65")

    def test_imported_bottle_of_perfume_sample2(self):
        self.product = Product("1 imported bottle of perfume at 27.99")
        result = self.product.saleOutput()
        self.assertEqual(result, "1 imported bottle of perfume: 32.19")

    def test_bottle_of_perfume_sample(self):
        self.product = Product("1 bottle of perfume at 18.99")
        result = self.product.saleOutput()
        self.assertEqual(result, "1 bottle of perfume: 20.89")

    def test_packet_of_headache_pills_sample(self):
        self.product = Product("1 packet of headache pills at 9.75")
        result = self.product.saleOutput()
        self.assertEqual(result, "1 packet of headache pills: 9.75")

    def test_box_of_imported_chocolates_sample(self):
        self.product = Product("1 box of imported chocolates at 11.25")
        result = self.product.saleOutput()
        self.assertEqual(result, "1 box of imported chocolates: 11.85")


if __name__ == '__main__':
    unittest.main()
