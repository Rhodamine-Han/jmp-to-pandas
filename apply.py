import pandas as pd

df = pd.read_csv('OS_test_sorter.csv')

def NANprocessing(i):
    if pd.notnull(i):
        return i
    else :
        return 1.00

df['Unnamed: 1'] = df['Unnamed: 1'].apply(NANprocessing)


print(df)