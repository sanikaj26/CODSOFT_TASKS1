import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("customer_data.csv")

print("CUSTOMER DATA ANALYSIS")
print("\nSummary Statistics:")
print(df.describe())

city_sales = df.groupby("City")["Purchase_Amount"].sum().sort_values(ascending=False)
product_sales = df.groupby("Product")["Purchase_Amount"].sum().sort_values(ascending=False)

bins = [0, 25, 35, 100]
labels = ["Young (0-25)", "Adult (26-35)", "Senior (36+)"]
df["Age_Group"] = pd.cut(df["Age"], bins=bins, labels=labels)
age_group_sales = df.groupby("Age_Group", observed=False)["Purchase_Amount"].sum()

top_customers = df.sort_values("Purchase_Amount", ascending=False).head(5)

print("\nSales by City:\n", city_sales)
print("\nSales by Product:\n", product_sales)
print("\nSales by Age Group:\n", age_group_sales)
print("\nTop 5 Customers:\n", top_customers[["Name","Purchase_Amount"]])

plt.figure(figsize=(8,5))
city_sales.plot(kind="bar")
plt.title("Total Purchase Amount by City")
plt.xlabel("City")
plt.ylabel("Purchase Amount")
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig("sales_by_city.png")

plt.figure(figsize=(8,5))
product_sales.plot(kind="bar")
plt.title("Total Purchase Amount by Product")
plt.xlabel("Product")
plt.ylabel("Purchase Amount")
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig("sales_by_product.png")

plt.figure(figsize=(8,5))
age_group_sales.plot(kind="bar")
plt.title("Customer Spending by Age Group")
plt.xlabel("Age Group")
plt.ylabel("Purchase Amount")
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig("sales_by_age_group.png")

df.to_csv("customer_analysis_results.csv", index=False)
print("\nAnalysis completed successfully!")
