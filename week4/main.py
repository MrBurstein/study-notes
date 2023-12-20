#For each unique sector, find highest funding 
### GRADED

ans4 = demographics.merge(right=use)
ans4 = ans4.merge(right=financials)
array = []
for value in ans4['sector'].unique():
    array.append( [ans4['funded_amount'][ans4['sector'] == value].sum(), value])
    print(array)
    
ans4 = max(array)
ans4 = ans4[1]
# Answer check
print(ans4)
print(type(ans4))

#For each unique sector, find highest ratio of total funding over total lender count

ans5 = demographics.merge(right=use)
ans5 = ans5.merge(right=financials)
ans5 = ans5.merge(right=crowdsource)


ans5.describe()
array = []
for value in ans5['sector'].unique():
    temp = ans5['funded_amount'][ans5['sector'] == value].sum()
    temp2 = ans5['lender_count'][ans5['sector'] == value].sum()
    ratio = temp / temp2
    array.append([ratio, value])
    print(array)
    
ans5 = max(array)
ans5 = ans5[1]

# Answer check
print(ans5)
print(type(ans5))