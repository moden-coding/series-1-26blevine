import unittest

from series_practice_1 import *

class TestElectronicsStoreSalesAnalysis(unittest.TestCase):

    def test_get_total_sales(self):
        self.assertEqual(get_total_sales(sales_series), 14350)

    def test_get_date_with_highest_sales(self):
        self.assertEqual(get_date_with_highest_sales(sales_series), "2023-10-13")

    def test_get_average_sales(self):
        self.assertAlmostEqual(get_average_sales(sales_series), 2050, 2)

    def test_get_days_with_sales_above(self):
        self.assertEqual(get_days_with_sales_above(sales_series, 2000), ["2023-10-11", "2023-10-12", "2023-10-13", "2023-10-15", "2023-10-16"])

    def test_get_sales_on_selected_days(self):
        self.assertEqual(get_sales_on_selected_days(sales_series, [0, 3, 5]), [1500, 2400, 2200])

if __name__ == '__main__':
    unittest.main()
