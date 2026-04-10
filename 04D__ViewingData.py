
import pandas as pd

df = pd.read_json("04Z_ASSET_jsnExample.json")
print(df)

print("_________________df.head()_________________________")
print(df.head())

print("_________________df.head(10)_________________________")
print(df.head(10))

print("_________________df.to_string()_________________________")
print(df.to_string())

print("_________________df.info()_________________________")
print(df.info())

print("_________________df.describe()_________________________")
print(df.describe())

