import pandas as pd

df = pd.read_csv('OS_test_sorter.csv')


Numofsam = int(input('How many samples? : '))
Numofref = int(input('How many references? : '))

# separating data
df_ref_raw = df.loc[0:((6*Numofref)-2)]
df_data_raw = df.loc[((6*Numofref)-2)+1:]
df_data_result = df_data_raw

df_ref_mean = df_ref_raw.groupby('OS1').mean()


for i in range(0, Numofsam - Numofref):
    df_data_result.iloc[6*i+1:6*i+5, 0] = df_ref_mean.iloc[0:4,0]
    df_data_result.iloc[6*i+1:6*i+5, 2] = df_ref_mean.iloc[0:4,1]

print(df_data_result)


df_data_result.to_csv('output.csv')