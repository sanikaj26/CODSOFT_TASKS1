import pandas as pd

# Load the dataset
df = pd.read_csv("cleaned_data.csv")

# Display the first 5 rows
print(df.head())
# Display basic information about the dataset
print("\nDataset Information:")
print(df.info())

# Descriptive statistics
print("\nDescriptive Statistics:")
print(df.describe())

# Check the number of rows and columns
print("\nDataset Shape:")
print(df.shape)
# Total sales for each product
print("\nSales by Product:")
product_sales = df.groupby("Product")["Price"].sum()
print(product_sales)

# Total sales by city
print("\nSales by City:")
city_sales = df.groupby("City")["Price"].sum()
print(city_sales)

# Average price by product
print("\nAverage Price by Product:")
avg_product_price = df.groupby("Product")["Price"].mean()
print(avg_product_price)

# Quantity sold by product
print("\nQuantity Sold by Product:")
quantity_by_product = df.groupby("Product")["Quantity"].sum()
print(quantity_by_product)
# Detect outliers using the IQR method

Q1 = df["Price"].quantile(0.25)
Q3 = df["Price"].quantile(0.75)

IQR = Q3 - Q1

lower_limit = Q1 - 1.5 * IQR
upper_limit = Q3 + 1.5 * IQR

outliers = df[(df["Price"] < lower_limit) | (df["Price"] > upper_limit)]

print("\nPrice Outliers:")
print(outliers)

print("\nNumber of Price Outliers:", len(outliers))
# Business Questions

print("\n--- Business Insights ---")

# 1. Most expensive product
most_expensive = df.loc[df["Price"].idxmax()]
print("Most expensive purchase:")
print(most_expensive)

# 2. Most frequently purchased product
most_purchased = df.groupby("Product")["Quantity"].sum().idxmax()
print("\nMost purchased product:", most_purchased)

# 3. City with highest quantity purchased
top_city = df.groupby("City")["Quantity"].sum().idxmax()
print("City with highest quantity purchased:", top_city)

# 4. Average customer age
average_age = df["Age"].mean()
print("Average customer age:", round(average_age, 2))
import matplotlib.pyplot as plt

# 1. Sales by Product
product_sales.plot(kind="bar")
plt.title("Sales by Product")
plt.xlabel("Product")
plt.ylabel("Sales")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# 2. Quantity Sold by Product
quantity_by_product.plot(kind="bar")
plt.title("Quantity Sold by Product")
plt.xlabel("Product")
plt.ylabel("Quantity")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# 3. Age Distribution
df["Age"].plot(kind="hist", bins=10)
plt.title("Customer Age Distribution")
plt.xlabel("Age")
plt.ylabel("Number of Customers")
plt.tight_layout()
plt.show()