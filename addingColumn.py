import pandas as pd

df = pd.read_csv('OS_test_sorter.csv')

df['Unnamed: 4'] = df['Unnamed: 1'] + 123

print(df)