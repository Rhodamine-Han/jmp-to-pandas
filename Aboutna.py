import pandas as pd

df = pd.read_csv('OS_test_sorter.csv')

#fillna
# df.fillna('', inplace=True)
# print(df)

#dropna
df.dropna(inplace=True)
print(df)