##index

#Data Frame
# import pandas as pd


# data = {
#     'Uni' : ['Kyushu', 'Seoul', 'Tokyo'], 'Conpany' : ['LGinnotek', 'Samsung Electrics', 'SK hynics'], 'name' : ['Rhodamine', 'Ted', 'Hines']
# }

#df stands for data frame
# df = pd.DataFrame(data, index = ['Student1', 'Student2', 'Student3'])

#reset
# df.index.name = 'students information'
# df.reset_index()

#reset and get rid of previous index
# df.index.name = 'students information'
# df.reset_index(drop=True, inplace=True)

#setting uni as the index
#inplace = setting those data as real data
# df.set_index('Uni', inplace=True)
# df

#sorting

# df.set_index('Uni', inplace=True)
# df.sort_index()