"""Delivery & Returns Analysis — Abatar Bhattarai
Clean a messy orders CSV with pandas, then summarise return rate by category, shipping and region.
Run:  python analysis.py
Input: orders_raw.csv   Output: orders_clean.csv + printed summary
"""
import pandas as pd
df = pd.read_csv("orders_raw.csv")
print(f"Raw rows: {len(df)}")
df = df.drop_duplicates()
df["region"] = df["region"].fillna("Unknown")
df.to_csv("orders_clean.csv", index=False)
print(f"Clean rows: {len(df)}")
print(f"Return rate: {(df['returned']=='Yes').mean()*100:.1f}%")
print("\nReturn rate by category:\n", df.groupby("category")["returned"].apply(lambda s: (s=="Yes").mean()*100).sort_values(ascending=False))
print("\nReturn rate by shipping:\n", df.groupby("shipping")["returned"].apply(lambda s: (s=="Yes").mean()*100))
print("\nAvg delivery days, returned vs kept:\n", df.groupby("returned")["delivery_days"].mean())
