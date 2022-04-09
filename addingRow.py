import pandas as pd

df = pd.read_csv('OS_test_sorter.csv')

df.loc[40] = ['D8N', 0.124,'D8N',10.24]

print(df)