import pandas as pd

dates = ["2023-10-10", "2023-10-11", "2023-10-12", "2023-10-13", "2023-10-14", "2023-10-15", "2023-10-16"]
sales = [1500, 2300, 2100, 2400, 1800, 2200, 2050]

# Creating a Pandas Series with dates as the index
sales_series = pd.Series(data=sales, index=dates)

def get_total_sales(sales_data):
    pass


def get_date_with_highest_sales(sales_data):
    pass



def get_average_sales(sales_data):
    pass


def get_days_with_sales_above(sales_data, threshold):
    pass


def get_sales_on_selected_days(sales_data, indices):
    pass
