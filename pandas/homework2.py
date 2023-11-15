# import data from pandas
import pandas as pd
import os

#create the DataFrame utilizing Pandas 
data = pd.read_csv('pandas/Crime_Data_from_2020_to_Present.csv') 

#generate all info for this dataset
data.info()

df = pd.DataFrame(data)

# Convert 'Date Rptd' column to datetime with the specified format
df['date'] = pd.to_datetime(df['Date Rptd'], format='%m/%d/%Y %I:%M:%S %p')

# Extract the year from the 'date' column
df['year'] = df['date'].dt.year

# Group by year and calculate the count of rows for each year
count_by_year = df.groupby('year').size().reset_index(name='count')

# Use Pandas built-in plotting
count_by_year.plot(kind='bar', x='year', y='count', legend=False).get_figure().savefig('bar_chart.jpg')



# Customize the plot
# (Optional) You can customize the plot using additional Pandas plotting options here

# Show the plot
# df = pd.DataFrame(data)
# df['date'] = pd.to_datetime(df['Date Rptd'], format=date_format)  # Convert 'date' column to datetime
# df['year'] = df['date'].dt.year
# sum_by_year = df.groupby('year').sum().reset_index()
# sum_by_year.plot(kind='bar', x='year', y='value', legend=False)
# plt.figure.savefig('demo-file.pdf')

#HISTOGRAM
# ax = data.plot.hist()
# ax.figure.savefig('demo-file.pdf')


#SCAT
# scat = data.plot(kind = 'scatter' , x='Date' , y='Salary' )
# scat = scat.figure.savefig('demo-file.pdf')


#LINE
# data = data.filter(items=['Team', 'Name', 'Salary'])
# data = data.loc[data.Team == 'Golden State Warriors', 'Name':'Salary']
# data.set_index('Name')
# lines = data.plot(kind = 'line', x='Name' , y='Salary' )
# lines.figure.savefig('demo-file.pdf')


#BAR
# bar = teamdata.plot(kind = 'bar', x='Name' , y='Salary' )
# bar.figure.savefig('demo-file.pdf')
# print(bar)
