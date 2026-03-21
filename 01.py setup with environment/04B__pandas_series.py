import pandas as pd

print("AAAAAAAAAAAAAAAA..........series....................")
a = [1, 7, 2]

myvar = pd.Series(a)

print(myvar)

print("BBBBBBBBBBB...............Dataframes....................")

data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}

myvar = pd.DataFrame(data)

print(myvar)

print("CCCCCCCCCCCCCCCC...............Dataframes....................")

data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}

#load data into a DataFrame object:
df = pd.DataFrame(data)

print(df) 