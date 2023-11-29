ans1 = gapminder.groupby('year')[['lifeExp']].mean()
ans2 = gapminder.groupby('continent')[["gdpPercap"]].median()

ans3 = gapminder.groupby('continent')[["gdpPercap"]].agg(['mean', 'median', 'std'])

#numerical condition
ans4 = gapminder.groupby(gapminder['pop'] > 300000000)[["lifeExp"]].mean()

#just something interesting to do
#ans5a = gapminder.groupby([gapminder['continent'] == 'Americas', gapminder['continent'] == 'Europe']).mean("lifeExp")
#ans5a = gapminder.query("continent == 'Americas' or continent == 'Europe'")

ans5a = gapminder[gapminder['continent'].isin(['Americas', 'Europe'])]
print(ans5a)
ans5b = ans5a.groupby('continent')[['lifeExp']].mean()
print(ans5b)

ans1 = gapminder.groupby('continent')[['lifeExp']].mean()
ans1 = ans1.sort_values(ascending=False, by='lifeExp')

ans2 = gapminder.groupby('country')[['gdpPercap']].mean()
ans2 = ans2.sort_values(ascending=False, by='gdpPercap')
ans2 = ans2.iloc[0].name

#### Sorting Results of Multiple Aggregates
ans3a = gapminder.groupby('continent')[["lifeExp"]].agg(['mean', 'median', 'std'])
ans3a.columns = [" ".join(c) for c in ans3a.columns.to_flat_index()]
ans3b = ans3a.sort_values(ascending=False, by='lifeExp median')

# Answer check
print(ans3a)
print(ans3b)

def column_range(x):
    '''
    This function takes in a pandas series and returns
    the range of the series (max - min) as a float.
    '''
    return x.max() - x.min()
    pass

# Answer check
column_range(gapminder['lifeExp'])
ans5 = gapminder.groupby('continent')[['gdpPercap']].apply(column_range).sort_values(by = 'gdpPercap', ascending = False)


### GRADED
# Grouping by 'Year' and calculating the total GDP for each year
total_world_gdp = gapminder.groupby('year')['gdpPercap'].sum()

# Calculating each country's share of world GDP by year
gapminder['Share_of_World_GDP'] = gapminder.apply(lambda row: row['gdpPercap'] / total_world_gdp[row['year']], axis=1)

# Creating a new DataFrame 'ans3' with the calculated share of world GDP for each country by year
ans3 = gapminder[['year', 'country', 'Share_of_World_GDP']]


# Answer check
print(ans3.head())
print(ans3.shape, gapminder.shape)

### GRADED

list_of_countries = ['China', 'United States', 'Japan', 'India', 'United Kingdom', 'Germany']
ans5a = None
ans5b = None
# List of countries
countries_list = ['Country1', 'Country2', 'Country3']  # Add your list of countries here

# # Filtering the DataFrame 'ans4' for the list of countries
# filtered_data = ans4[ans4['country'].isin(countries_list)]

# Creating the line plot
plt.figure(figsize=(10, 6))  # Adjust the figure size if needed
lineplot = sns.lineplot(data=ans4, x='year', y='gdpPercap', hue='country')

# Adding title and labels
lineplot.set_title('Top Countries Share of GDP 1952 - 2002')
lineplot.set_xlabel('Year')
lineplot.set_ylabel('Share of World GDP')

# Assigning the plot to 'ans5a' (assuming you're storing the plot)
ans5a = lineplot


### GRADED

ans5a = None
ans5b = None
# List of countries

countries_list = ['China', 'United States', 'Japan', 'India', 'United Kingdom', 'Germany']

# # Filtering the DataFrame 'ans4' for the list of countries
filtered_data = ans4[ans4['country'].isin(countries_list)]

# Creating the line plot
plt.figure(figsize=(10, 6))  # Adjust the figure size if needed
lineplot = sns.lineplot(data=filtered_data, x='year', y='gdpPercap', hue='country')

# Adding title and labels
lineplot.set_title('Top Countries Share of GDP 1952 - 2002')
lineplot.set_xlabel('Year')
lineplot.set_ylabel('Share of World GDP')

# Assigning the plot to 'ans5a' (assuming you're storing the plot)
ans5a = lineplot

#1
ans1 = gapminder.groupby('year')[['gdpPercap']].agg(sum)

#22
ans2_ = gapminder_.set_index(['year', 'country'])

#333
ans3_ = gapminder_.set_index(['year', 'country'])/gapminder_.groupby('year').sum()

#44
ans4_ = (gapminder_.set_index(['year', 'country'])/gapminder_.groupby('year').sum())[['gdpPercap']].reset_index()

#555
list_of_countries = ['China', 'United States', 'Japan', 'India', 'United Kingdom', 'Germany']
ans5a = ans4.query("country in @list_of_countries")

sns.lineplot(data = ans5a, x = 'year', y = 'gdpPercap', hue = 'country')
plt.title('Share of GDP')
plt.xlabel('Year')
plt.ylabel("GDP per capita")

ans2 = gapminder.groupby('country').filter(lambda x: x['pop'].mean() > 20000000)
