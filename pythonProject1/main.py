# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from FileOperation import FileOperation
from SalesData import SalesData
def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
FileOperation=FileOperation()
file=FileOperation.read_csv("YafeNof.csv")
s=SalesData(file)
s.analyze_sales_data()
s.bar_chart_category_sum()
print(s.filter_by_sellings_or())
print(s.filter_by_sellings_end())
print(s.divide_by_2())
s.save_modified_sales_data()
s.task_6_1_sns()
s.task_6_2_sns()
s.task_6_3_sns()
s.task_6_4_sns()
s.task_6_5_sns()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
