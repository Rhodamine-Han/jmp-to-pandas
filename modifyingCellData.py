import pandas as pd

df = pd.read_csv('OS_test_sorter.csv')

df.loc[38,'Unnamed: 2'] = 1234

print(df)