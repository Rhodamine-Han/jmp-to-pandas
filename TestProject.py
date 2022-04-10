import pandas as pd

df = pd.read_csv('OS_test_sorter.csv')


# #already made how to do numbering

# count = 0

# Numofsam = int(input('number of data? : '))

# df['Unnamed: 4'] = 0

# while True:
#     if count < Numofsam:
#         df['Unnamed: 4'][count*6:count*6+4] = count+1
#         count += 1
#     else:
#         break


Numofsam = int(input('How many samples? : '))
Numofref = int(input('How many references? : '))

df_ref_raw = df.loc[0:((6*Numofref)-2)]

df_ref_D0N = df_ref_raw.groupby('OS1').get_group('D0N')
df_ref_D0P = df_ref_raw.groupby('OS1').get_group('D0P')
df_ref_D1N = df_ref_raw.groupby('OS1').get_group('D1N')
df_ref_D1P = df_ref_raw.groupby('OS1').get_group('D1P')

print(df_ref_D0N)


