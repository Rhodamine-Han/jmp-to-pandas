import pandas as pd

df = pd.read_csv('OS_test_sorter.csv')

df.sort_values('Unnamed: 1', inplace=True)
print(df)

