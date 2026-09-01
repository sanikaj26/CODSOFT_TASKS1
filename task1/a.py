import pandas as pd

# Load dataset
df = pd.read_csv("sales_data.csv")

print("----- ORIGINAL DATA -----")
print(df.head())

# Check missing values
print("\n----- MISSING VALUES BEFORE CLEANING -----")
print(df.isnull().sum())

# Check duplicate customers based on Name, Age, Gender, City, Product, Quantity, Price, Purchase_Date
print("\n----- DUPLICATES BEFORE CLEANING -----")
duplicate_rows = df.duplicated(
    subset=["Name", "Age", "Gender", "City", "Product",
            "Quantity", "Price", "Purchase_Date"]
).sum()
print(duplicate_rows)

# Remove duplicate records
df = df.drop_duplicates(
    subset=["Name", "Age", "Gender", "City", "Product",
            "Quantity", "Price", "Purchase_Date"]
)

# Fill missing Age with median
df["Age"] = df["Age"].fillna(df["Age"].median())

# Fill missing Price with median
df["Price"] = df["Price"].fillna(df["Price"].median())

# Correct inconsistent Gender
df["Gender"] = df["Gender"].str.strip().str.title()

# Correct inconsistent City
df["City"] = df["City"].str.strip().str.title()

# Convert Purchase_Date to datetime
df["Purchase_Date"] = pd.to_datetime(df["Purchase_Date"])

# Check cleaned data
print("\n----- MISSING VALUES AFTER CLEANING -----")
print(df.isnull().sum())

print("\n----- DUPLICATES AFTER CLEANING -----")
print(df.duplicated(
    subset=["Name", "Age", "Gender", "City", "Product",
            "Quantity", "Price", "Purchase_Date"]
).sum())

# Save cleaned dataset
df.to_csv("cleaned_data.csv", index=False)
print("\nCleaning completed successfully!")
print("Saved as cleaned_data.csv")