
#A Pandas DataFrame is a 2 dimensional data structure, like a 2 dimensional array, or a table with rows and columns

import pandas as pd

df = pd.read_csv('04Z_ASSET_customers-100.csv')

print(df) 


print("22222222222222222222222222222222222222222222")

df = pd.read_csv('04Z_ASSET_customers-100.csv')

print(df.to_string()) 

print("333333333333333333333333333333333333333333333333333")

df = pd.read_json("04Z_ASSET_jsnExample.json")
print(df)



