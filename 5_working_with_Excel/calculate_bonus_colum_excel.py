import pandas as pd

employee_data = pd.read_excel('employee_data.xlsx')
product_data = pd.read_excel('input.xlsx')

print(employee_data)
print(employee_data.head())
print(employee_data.describe())

employee_data['Bonus'] = employee_data['Salary'] * 0.1
print(employee_data)

product_data['Total'] = product_data['Price'] * product_data['Quantity']
print(product_data)

employee_data.to_excel('added_bonus_employee_data.xlsx', index=False)
product_data.to_excel('output.xlsx', index=False)
