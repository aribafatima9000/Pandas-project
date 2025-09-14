import pandas as pd

data = {
    "Date": pd.date_range(start="2024-01-01", periods=10, freq="M"),
    "Product": ["Mobile","Laptop","TV","Tablet","Mobile","Laptop","TV","Tablet","Mobile","Laptop"],
    "Region": ["North","South","East","West","North","South","East","West","North","South"],
    "Sales": [1200,2500,1800,1600,2200,2700,2000,2100,2400,2600]
}

df = pd.DataFrame(data)

# Region wise total and average sales
print(df.groupby("Region")["Sales"].agg(["sum","mean"]))

# Top 3 products
print(df.groupby("Product")["Sales"].sum().nlargest(3))
