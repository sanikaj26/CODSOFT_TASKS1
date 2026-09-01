import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load cleaned data
df = pd.read_csv("cleaned_data.csv")

sns.set_style("whitegrid")
plt.rcParams["figure.figsize"] = (8, 5)

# 1. BAR CHART — Total sales by product
product_sales = df.groupby("Product")["Price"].sum().sort_values(ascending=False)
plt.figure()
sns.barplot(x=product_sales.index, y=product_sales.values, palette="viridis")
plt.title("Total Sales by Product")
plt.xlabel("Product")
plt.ylabel("Total Sales ($)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("visualizations/bar_sales_by_product.png")
plt.close()

# 2. LINE CHART — Sales trend over time (only if you have a Date column)
if "Date" in df.columns:
    df["Date"] = pd.to_datetime(df["Date"])
    daily_sales = df.groupby("Date")["Price"].sum()
    plt.figure()
    plt.plot(daily_sales.index, daily_sales.values, marker="o", color="teal")
    plt.title("Sales Trend Over Time")
    plt.xlabel("Date")
    plt.ylabel("Total Sales ($)")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig("visualizations/line_sales_trend.png")
    plt.close()

# 3. PIE CHART — Sales share by city
city_sales = df.groupby("City")["Price"].sum()
plt.figure()
plt.pie(city_sales.values, labels=city_sales.index, autopct="%1.1f%%", startangle=90,
        colors=sns.color_palette("pastel"))
plt.title("Sales Share by City")
plt.tight_layout()
plt.savefig("visualizations/pie_sales_by_city.png")
plt.close()

# 4. HISTOGRAM — Distribution of price
plt.figure()
sns.histplot(df["Price"], bins=20, kde=True, color="steelblue")
plt.title("Distribution of Price")
plt.xlabel("Price")
plt.ylabel("Frequency")
plt.tight_layout()
plt.savefig("visualizations/histogram_price.png")
plt.close()

# 5. SCATTER PLOT — Price vs Quantity (if Quantity exists), else Price vs index
if "Quantity" in df.columns:
    plt.figure()
    sns.scatterplot(x="Quantity", y="Price", data=df, hue="Product", alpha=0.7)
    plt.title("Price vs Quantity")
    plt.tight_layout()
    plt.savefig("visualizations/scatter_price_quantity.png")
    plt.close()

print("All charts saved to the visualizations/ folder.")