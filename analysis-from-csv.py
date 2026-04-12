import pandas as pd
# load data from CSV file
df = pd.read_csv("sales.csv")
# show first rows
print(df.head())
# total sales
print("Total Sales:", df["Sales"].sum())
# average sales
print("Average Sales:", df["Sales"].mean())
# sales by category
print("\nSales by Category:")
print(df.groupby("Category")["Sales"].sum())
# find best product
best_product = df.groupby("Product")["Sales"].sum().idxmax()
print("\nBest Product:", best_product)
