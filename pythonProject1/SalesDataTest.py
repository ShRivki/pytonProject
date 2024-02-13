import unittest
import pandas as pd
import numpy as np
from SalesData import SalesData

class TestSalesData(unittest.TestCase):

    def setUp(self):
        # Create a sample DataFrame for testing
        data = {
            'Date': ['01.01.2023', '02.01.2023', '03.01.2023'],
            'Product': ['A', 'B', 'A'],
            'Quantity': [10, 20, 30],
            'Total': [100, 200, 300],
            'Price': [5, 10, 15]
        }
        self.sales_data = SalesData(pd.DataFrame(data))

    def test_eliminate_duplicates(self):
        # Test if duplicates are eliminated properly
        self.sales_data.eliminate_duplicates()
        self.assertEqual(len(self.sales_data.data), 3)  # Assuming there are no duplicates in the sample data

    def test_calculate_total_sales(self):
        # Test if total sales calculation is correct
        total_sales = self.sales_data.calculate_total_sales()
        self.assertEqual(total_sales['A'], 40)  # Total sales of Product A should be 40

    def test_calculate_total_sales_per_month(self):
        # Test if total sales per month calculation is correct
        total_sales_per_month = self.sales_data._calculate_total_sales_per_month()
        self.assertEqual(total_sales_per_month[1], 600)  # Total sales in January should be 100

    def test_identify_best_selling_product(self):
        # Test if identification of the best selling product is correct
        best_selling_product = self.sales_data._identify_best_selling_product()
        self.assertEqual(best_selling_product, 'A')  # Product A should be the best selling product

    def test_identify_month_with_highest_sales(self):
        # Test if identification of the month with highest sales is correct
        month_with_highest_sales = self.sales_data._identify_month_with_highest_sales()
        self.assertEqual(month_with_highest_sales, 1)  # March should be the month with highest sales

    def test_analyze_sales_data(self):
        # Test if analysis of sales data returns correct dictionary
        analysis_result = self.sales_data.analyze_sales_data()
        self.assertEqual(analysis_result['best_selling_product'], 'A')
        self.assertEqual(analysis_result['month_with_highest_sales'], 1)

    def test_add_to_dicty_less_avg(self):
        # Test if addition to dictionary for least selling product and average sales per month is correct
        dicty = self.sales_data.add_to_dicty_less_avg()
        self.assertEqual(dicty['minimest_selling_product'], 'B')
        self.assertEqual(dicty['average_sales_per_month'], 600)

    def test_calculate_cumulative_sales(self):
        # Test if calculation of cumulative sales is correct
        cumulative_sales = self.sales_data.calculate_cumulative_sales()
        self.assertEqual(cumulative_sales[(1, 2023, 'A')], 40)

    def test_add_90_percent_values_column(self):
        # Test if addition of 90% values column is correct
        data_with_90_percent_values = self.sales_data.add_90_percent_values_column()
        self.assertTrue('sele90%' in data_with_90_percent_values.columns)

    # Add tests for the remaining functions...
    def test_calculate_mean_quantity(self):
        # Test if calculation of mean, median, and second maximum is correct
        mean, median, second_max = self.sales_data.calculate_mean_quantity()
        self.assertAlmostEqual(mean, 200.0)  # Mean should be 200
        self.assertEqual(median, 200)  # Median should be 200
        self.assertEqual(second_max, 200)  # Second maximum should be 200

if __name__ == '__main__':
    unittest.main()
