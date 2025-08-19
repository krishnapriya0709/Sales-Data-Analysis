import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv("/Users/krishnapriya/Downloads/Sales.csv")
print(df.head())
print(df.info())
print(df.describe())
print(df.isnull().sum())

print("Total Sales:", df['Sales'].sum())
print("Total Profit:", df['Profit'].sum())

print(df['Category'].value_counts())
category_sales = df.groupby('Category')['Sales'].sum()
print(category_sales)

region_sales = df.groupby('Region')['Sales'].sum()
print(region_sales)

category_sales.plot(kind='bar', title="Sales by Category")
plt.xlabel("Category")
plt.ylabel("Sales")
plt.show()






