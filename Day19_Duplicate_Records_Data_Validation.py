import pandas as pd

df = pd.read_csv("sales_data.csv")

# 1. Duplicate record analysis
print("Original rows:", len(df))
print("Duplicate rows:", df.duplicated().sum())
duplicate_records = df[df.duplicated(keep=False)]
print("Duplicate records:")
print(duplicate_records)
duplicate_records.to_csv("duplicate_records.csv", index=False)

# 2. Clean dataset
cleaned_df = df.drop_duplicates().copy()
cleaned_df.to_csv("sales_data_cleaned.csv", index=False)
print("Rows after removing duplicates:", len(cleaned_df))

# 3. Five+ validation checks
print("\nValidation 1 - Missing values:")
print(df.isna().sum())

print("\nValidation 2 - Duplicate rows:", df.duplicated().sum())

print("\nValidation 3 - Sales amount range:")
print("Negative Sales_Amount:", (df["Sales_Amount"] < 0).sum())

print("\nValidation 4 - Quantity range:")
print("Non-positive Quantity_Sold:", (df["Quantity_Sold"] <= 0).sum())

print("\nValidation 5 - Discount range:")
print("Discount outside 0 to 1:", ((df["Discount"] < 0) | (df["Discount"] > 1)).sum())

print("\nValidation 6 - Expected categories:")
print("Regions:", sorted(df["Region"].dropna().unique()))
print("Customer types:", sorted(df["Customer_Type"].dropna().unique()))
print("Sales channels:", sorted(df["Sales_Channel"].dropna().unique()))

print("\nValidation 7 - Region/Sales Rep consistency:")
expected = df["Region"].astype(str) + "-" + df["Sales_Rep"].astype(str)
print("Inconsistent rows:", (df["Region_and_Sales_Rep"].astype(str) != expected).sum())
