import pandas as pd
# create sample data
data = {
    "Product": ["A", "B", "C", "A", "B"],
    "Category": ["Electronics", "Clothing", "Electronics", "Clothing", "Electronics"],
    "Sales": [100, 200, 150, 300, 250]}
df = pd.DataFrame(data)
# show data
print(df)
# total sales
print("Total Sales:", df["Sales"].sum())
# sales by category
print(df.groupby("Category")["Sales"].sum())
