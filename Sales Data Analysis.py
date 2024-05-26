import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Load the data
sales_data = pd.read_csv('sales_data.csv')

# Step 2: Data Exploration
print(sales_data.head())  # Display the first few rows of the dataset
print(sales_data.info())  # Display information about the dataset

# Step 3: Data Cleaning
# Check for missing values
print(sales_data.isnull().sum())

# Drop rows with missing values
sales_data.dropna(inplace=True)

# Step 4: Data Analysis
# Total sales over a certain period
total_sales = sales_data['Sales Amount'].sum()
print("Total Sales Amount:", total_sales)

# Sales by product category
sales_by_category = sales_data.groupby('Category')['Sales Amount'].sum()
print("\nSales by Category:")
print(sales_by_category)

# Sales distribution across different regions
sales_by_region = sales_data.groupby('Region')['Sales Amount'].sum()
print("\nSales by Region:")
print(sales_by_region)

# Step 5: Data Visualization
# Bar plot for sales by category
sales_by_category.plot(kind='bar', xlabel='Category', ylabel='Sales Amount', title='Sales by Category')
plt.xticks(rotation=45)
plt.show()

# Pie chart for sales distribution by region
sales_by_region.plot(kind='pie', autopct='%1.1f%%', startangle=90, title='Sales Distribution by Region')
plt.ylabel('')
plt.show()

