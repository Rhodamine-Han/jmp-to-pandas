import pandas as pd

df = pd.read_csv('OS_test_sorter.csv')

# countFORGRP = 1
count = 0


# MyLen = len(df['Unnamed: 3'])

# while True:
#     if count < MyLen:
#         df['Unnamed: 4'] = countFORGRP
#     else:

NumofRef = int(input('number of ref.? : '))

df['Unnamed: 4'] = 0

# df['Unnamed: 4'][0:4] = 1

while True:
    if count < NumofRef:
        df['Unnamed: 4'][count*4:count*4+4] = count+1
        df['Unnamed: 4'][count*4+4:count*4+6] = 0
        count += 1

    else:
        break



print(df)
