import pandas as pd


data = {
    'Uni' : ['Kyushu', 'Seoul', 'Tokyo'], 'Conpany' : ['LGinnotek', 'Samsung Electrics', 'SK hynics'], 'name' : ['Rhodamine', 'Ted', 'Hines']
}

#df stands for data frame
df = pd.DataFrame(data, index = ['Student1', 'Student2', 'Student3'], columns = ['name', 'Uni'])

df