import pandas as pd

df = pd.read_csv('OS_test_sorter.csv')


# print(df.groupby('OS1').get_group('D1N'))
print(df.groupby('OS1').mean())