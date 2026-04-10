"""
Data cleaning means fixing bad data in your data set.

Bad data could be:

Empty cells
Data in wrong format
Wrong data
Duplicates

"""
import pandas as pd 

df = pd.read_csv("04Z_ASSET_customers-100.csv")

print(df.to_string())

new_df = df.dropna()
print(new_df)