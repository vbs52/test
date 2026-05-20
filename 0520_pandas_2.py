import pandas as pd


data1 = {
    "Product": ["Apple", "Banana", "Orange", "Mango", "Grape", "Guava"],
    "Price": [30, 20, 25, 60, 45, 35],
    "Sales": [100, 150, 80, 60, 90, 54]
}

df1 = pd.DataFrame(data1)


data2 = [
    ["Apple", 30, 100],
    ["Banana", 20, 150],
    ["Orange", 25, 80],
    ["Mango", 60, 60],
    ["Grape", 45, 90],
    ["Guava", 35, 54]
]

df2 = pd.DataFrame(data2, columns=["Product", "Price", "Sales"])

print(df1.head())

print(df1.tail())

print(df1.shape)

print(df1.columns)

print(df1.dtypes)

print(df1.count())

stats = df1.describe().round(2)

print(stats)


stats.to_csv("0520_stock2.csv")