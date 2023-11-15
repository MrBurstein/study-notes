
url = 'https://raw.githubusercontent.com/mwaskom/seaborn-data/master/diamonds.csv'

import pandas as pd

diamonds = ''

diamonds = pd.read_csv(url)

print(type(diamonds))
print("#####################################")
print("'Head()' method will print top 10 data poins")

print(diamonds.head()) 

print("#####################################")
print("'info()' method will display collumn names and their data types")

print(diamonds.info())

print("#####################################")
print("'describe()' method will print display count/mean/std/min/max")

print(diamonds.describe())

# This is format to locate loc(index, collumn selector)
# teamdata = data.loc[data['Name'] == 'LeBron James' , ['Name', 'Team']]

