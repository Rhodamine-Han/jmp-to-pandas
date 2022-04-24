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

# getting the number of samples, ref.
Numofsam = int(input('How many samples? : '))
Numofref = int(input('How many references? : '))

# separating data
df_ref_raw = df.loc[0:((6*Numofref)-2)]
df_data_raw = df.loc[((6*Numofref)-2)+1:]
df_data_raw_2 = df_data_raw

# seperating by pins
#df_ref_D0N = df_ref_raw.groupby('OS1').get_group('D0N')
# df_ref_D0P = df_ref_raw.groupby('OS1').get_group('D0P')
# df_ref_D1N = df_ref_raw.groupby('OS1').get_group('D1N')
# df_ref_D1P = df_ref_raw.groupby('OS1').get_group('D1P')

# mean
df_ref_mean = df_ref_raw.groupby('OS1').mean()

# Forward
# df_ref_mean_D0N_For = df_ref_raw.groupby('OS1').get_group('D0N').mean()[0]
# df_ref_mean_D0P_For = df_ref_raw.groupby('OS1').get_group('D0P').mean()[0]
# df_ref_mean_D1N_For = df_ref_raw.groupby('OS1').get_group('D1N').mean()[0]
# df_ref_mean_D1P_For = df_ref_raw.groupby('OS1').get_group('D1P').mean()[0]

# reverse
# df_ref_mean_D0N_Rev = df_ref_raw.groupby('OS1').get_group('D0N').mean()[1]
# df_ref_mean_D0P_Rev = df_ref_raw.groupby('OS1').get_group('D0P').mean()[1]
# df_ref_mean_D1N_For = df_ref_raw.groupby('OS1').get_group('D1N').mean()[1]
# df_ref_mean_D1P_For = df_ref_raw.groupby('OS1').get_group('D1P').mean()[1]


# for i in range(1, (Numofsam - Numofref), 1):
#     df_data_raw_2['OS1'][(6*(i-1)):6*i-1] = [{'', str(df_ref_mean_D0N_For), str(df_ref_mean_D0P_For), str(df_ref_mean_D1N_For), str(df_ref_mean_D1P_For), ''}]
#     df_data_raw_2['Unnamed: 3'][(7*(i-1)):7*i] = [{'', str(df_ref_mean_D0N_Rev), str(df_ref_mean_D0P_Rev), str(df_ref_mean_D1N_For), str(df_ref_mean_D1P_For), ''}]

# using iloc
# for i in range(1, (Numofsam - Numofref), 1):
#     df_data_raw_2.iloc[]


#just use this one then it's all over!!

df_data_raw_2.iloc[1:5, 0] = df_ref_mean.iloc[0:4,0]


print(df_data_raw_2)

#1~4 7~10