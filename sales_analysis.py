import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
data = pd.read_csv("sales_data.csv")

# Create Total Sales column
data["Total_Sales"] = data["Price"] * data["Quantity"]

# Display data
print("Sales Dataset:\n")
print(data)

# Category-wise total sales
category_sales = data.groupby("Category")["Total_Sales"].sum()

print("\nCategory Wise Sales:\n")
print(category_sales)

# Visualization
category_sales.plot(kind="bar")

plt.title("Total Sales by Category")
plt.xlabel("Category")
plt.ylabel("Total Sales")
plt.tight_layout()
plt.show()
