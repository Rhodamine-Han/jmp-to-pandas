import pandas as pd

df = pd.read_csv('OS_test_sorter.csv')

cols = list(df.columns)
df = df[[cols[-1]]+ cols[0:-1]]

print(df)