import pandas as pd

dates = ["2023-10-10", "2023-10-11", "2023-10-12", "2023-10-13", "2023-10-14", "2023-10-15", "2023-10-16"]
sales = [1500, 2300, 2100, 2400, 1800, 2200, 2050]

# Creating a Pandas Series with dates as the index
sales_series = pd.Series(data=sales, index=dates)
thresh=2000
ind=[1, 3, 5]


def get_total_sales(sales_data):
    print(sales_data.sum())
    pass


def get_date_with_highest_sales(sales_data):
    print(sales_data.idxmax())
    pass



def get_average_sales(sales_data):
    print(sales_data.mean())
    pass


def get_days_with_sales_above(sales_data, threshold):
    print(sales_data[sales_data > threshold].index.tolist())
    pass


def get_sales_on_selected_days(sales_data, indices):
    print(sales_data[indices])


get_total_sales(sales_series)
get_date_with_highest_sales(sales_series)
get_average_sales(sales_series)
get_days_with_sales_above(sales_series, thresh)
get_sales_on_selected_days(sales_series, ind)


