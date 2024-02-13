import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
from FileOperation import FileOperation
import random
import sys
import datetime


class SalesData:
    def __init__(self, data):
        self.data = data
        self.data['Date'] = pd.to_datetime(self.data['Date'], dayfirst=False, format='%d.%m.%Y')

    # מוחק שורות כפולות
    def eliminate_duplicates(self):
        self.data = self.data.drop_duplicates()

    # מחשב כמות לכל מוצר
    def calculate_total_sales(self):
        total_sales = self.data.groupby('Product')['Quantity'].sum()
        return total_sales

    # מחשב בכמה מכרו לכל חודש
    def _calculate_total_sales_per_month(self):
        # self.data['Date'] = pd.to_datetime(self.data['Date'], dayfirst=False, format='%d.%m.%Y')
        total_sales_per_month = self.data.groupby(self.data['Date'].dt.month)['Total'].sum()
        return total_sales_per_month

    # מהמוצר שנקנה הכי הרבה
    def _identify_best_selling_product(self):
        best_selling_product = self.calculate_total_sales().idxmax()
        return best_selling_product

    # החודש שקנו הכי הרבה
    def _identify_month_with_highest_sales(self):
        month_with_highest_sales = self._calculate_total_sales_per_month().idxmax()
        return month_with_highest_sales

    # מילון של המוצר שקנו הכי הרבהוחודש שקנו הכי הרבה
    def analyze_sales_data(self):
        dicty = {}
        dicty['best_selling_product'] = self._identify_best_selling_product()
        dicty['month_with_highest_sales'] = self._identify_month_with_highest_sales()
        return dicty

    #  את המוצר שנקנה הכי פחות ואת ממוצע מכירות מוסיף למילון
    def add_to_dicty_less_avg(self):
        dicty = self.analyze_sales_data()
        dicty['minimest_selling_product'] = self.calculate_total_sales().idxmin()
        dicty['average_sales_per_month'] = self._calculate_total_sales_per_month().mean()
        return dicty

    # לכל מוצר כמה נקנה בחודש מסוים
    def calculate_cumulative_sales(self):
        total_sales_per_month = \
            self.data.groupby([self.data['Date'].dt.month, self.data['Date'].dt.year, self.data['Product']])[
                'Quantity'].sum()
        return total_sales_per_month

    # עמודה של 90 %  הנחה מוסיף
    def add_90_percent_values_column(self):
        self.data["sele90%"] = self.data['Price'] * 0.9
        return self.data

    # שרטוט של מוצר לפי כמות
    def bar_chart_category_sum(self):
        product_sales = self.data.groupby('Product')['Quantity'].sum().reset_index()
        plt.figure(figsize=(10, 6))
        sns.barplot(x='Product', y='Quantity', data=product_sales)
        plt.savefig('Sum_Product.png')
        # plt.show()
        plt.savefig("sum_product.png")

    # מחזיר ממוצע חציון ומקסימום שני
    def calculate_mean_quantity(self):
        return np.mean(self.data["Total"]), np.median(self.data["Total"]), np.sort(self.data["Total"])[-2]

    def filter_by_sellings_or(self):
        p = self.data
        return p[(p['Quantity'] > 5) | (p['Quantity'] == 0)]

    def filter_by_sellings_end(self):
        p = self.data
        return p[(p['Quantity'] > 2) & (p['Price'] > 300)]

    # עמודת BlackFridayPrice
    def divide_by_2(self):
        self.data["BlackFridayPrice"] = self.data['Price'] / 2
        return self.data

    # 27
    def save_modified_sales_data(self):
        file_operation = FileOperation()
        df_analyzed = pd.DataFrame(self.analyze_sales_data().items(), columns=['Metric', 'Value'])
        file_operation.save_to_csv(df_analyzed, 'analyze_sales_data.csv')

    # task 6
    # ==============plt================

    # ============sns=================
    def task_6_1_sns(self):
        per_month = self._calculate_total_sales_per_month().reset_index()
        plt.figure(figsize=(10, 6))
        sns.barplot(x='Date', y='Total', data=per_month)
        # plt.show()
        try:
            plt.savefig("task_6_1_sns.png")
        except Exception as e:
            self.error(e)

    def task_6_2_sns(self):
        p = self._calculate_total_sales_per_month().reset_index()
        plt.figure(figsize=(10, 6))
        sns.lmplot(x='Date', y='Total', data=p)
        # plt.show()
        try:
            # plt.show()
            plt.savefig("task_6_2_sns.png")
        except Exception as e:
            self.error(e)

    def task_6_3_sns(self):
        p = self._calculate_total_sales_per_month().reset_index()
        plt.figure(figsize=(10, 6))
        sns.lineplot(x='Date', y='Total', data=p)
        # plt.show()
        try:
            plt.savefig("task_6_3_sns.png")
        except Exception as e:
            self.error(e)

    def task_6_4_sns(self):
        p = self._calculate_total_sales_per_month().reset_index()
        plt.figure(figsize=(10, 6))
        sns.scatterplot(x='Date', y='Total', data=p)
        # plt.show()
        try:
            plt.savefig("task_6_4_sns.png")
        except Exception as e:
            self.error(e)

    def task_6_5_sns(self):
        p = self._calculate_total_sales_per_month().reset_index()
        plt.figure(figsize=(10, 6))
        sns.boxenplot(x='Date', y='Total', data=p)
        # plt.show()
        try:
            plt.savefig("task_6_5_sns.png")
        except Exception as e:
            self.error(e)

    def task_6_1_plt(self):
        p = self._calculate_total_sales_per_month().reset_index()
        plt.figure(figsize=(10, 6))
        plt.plot(p['Date'], p['Total'])
        plt.savefig("task_6_1_plt.png")

    def task_6_2_plt(self):
        p = self._calculate_total_sales_per_month().reset_index()
        plt.figure(figsize=(10, 6))
        plt.bar(p['Date'], p['Total'])
        plt.grid(True)
        plt.savefig("task_6_2_plt.png")

    def task_6_3_plt(self):
        p = self._calculate_total_sales_per_month().reset_index()
        plt.figure(figsize=(10, 6))
        plt.scatter(p['Date'], p['Total'])
        plt.grid(True)
        plt.savefig("task_6_3_plt.png")

    def task_6_4_plt(self):
        p = self._calculate_total_sales_per_month().reset_index()
        plt.figure(figsize=(10, 6))
        plt.violinplot(p['Total'])
        plt.grid(True)
        plt.savefig("task_6_4_plt.png")

    def task_6_5_plt(self):
        p = self._calculate_total_sales_per_month().reset_index()
        plt.figure(figsize=(10, 6))
        plt.boxplot(p['Total'])
        plt.grid(True)
        plt.savefig("task_6_5_plt.png")

    def task_6_6_plt(self):
        p = self._calculate_total_sales_per_month().reset_index()
        plt.figure(figsize=(10, 6))
        plt.fill_between(p['Date'], p['Total'])
        plt.grid(True)
        plt.savefig("task_6_6_plt.png")

    def task_6_7_plt(self):
        p = self._calculate_total_sales_per_month().reset_index()
        plt.figure(figsize=(10, 6))
        plt.polar(p['Date'], p['Total'])
        plt.grid(True)
        plt.savefig("task_6_7_plt.png")

    ###משימה 7

    # 1
    def error(self, error: str):
        print('<{0},{1} >,type error:{2}<{0}>'.format('rivki', datetime.datetime.now().strftime("%d.%m.%y, %H:%M"),
                                                      error))

    # 2 נמצא בFILE OPERTION
    # 3
    def randomi(self, name: str):
        result = []
        total_sales = self.calculate_total_sales()
        if name in total_sales.index:
            count = total_sales[name]  # Assuming the value is the total sales count
        result.append(count)
        max_price_product = self.data.groupby(['Product']).max('Price')
        if name in max_price_product.index:
            max_price = max_price_product.loc[name, 'Price']  # Assuming the value is the total sales count
        result.append(max_price)
        if count>max_price:
            num=random.randint(max_price,count)
        else:
            num = random.randint( count,max_price)
        result.append(num)
        return result
    #4
    def version(self):
        return sys.version
    #5
    def process_parameters(self, *args,**kwargs):
        dicty = {}
        for key, value in kwargs.items():
            if value is not None:
                dicty[key] = value
        for value in args:
            if isinstance(value, int):
                print(value)
        return dicty
    #6
    def print_tabel(self):
        print(self.data.head(3));
        print(self.data.tail(2));
        print(self.data.iloc[random.randint(0,len(self.data)-1)]);

#7
    def pass_table(self):
        data_array = self.data.select_dtypes(include=['number']).values
        for value in np.nditer(data_array):
            print(value)