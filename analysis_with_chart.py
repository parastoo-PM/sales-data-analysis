import pandas as pd
import matplotlib.pyplot as plt
# create sample data
data = {
    "Product": ["A", "B", "C", "A", "B", "C"],
    "Category": ["Electronics", "Clothing", "Electronics", "Clothing", "Electronics", "Clothing"],
    "Sales": [100, 200, 150, 300, 250, 180]}
df = pd.DataFrame(data)
# total sales
total_sales = df["Sales"].sum()
print("Total Sales:", total_sales)
# sales by category
category_sales = df.groupby("Category")["Sales"].sum()
print("\nSales by Category:\n", category_sales)
# plot bar chart
category_sales.plot(kind="bar")
plt.title("Sales by Category")
plt.xlabel("Category")
plt.ylabel("Sales")
plt.show()
