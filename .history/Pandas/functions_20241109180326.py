import pandas as pd

data = {
    'Name' : ['Atharv','Piyush','Alfaj'],
    'Age' : [20,21,21],
    'city' : ['Vita','Kolhapur','Islampur']
}

df = pd.DataFrame(data)
print(df)