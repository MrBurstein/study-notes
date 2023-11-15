# import data from pandas
import pandas as pd
import os

#https://www.kaggle.com/datasets/ishmaelkiptoo/motor-vehicle-collisions/download?datasetVersionNumber=1
#https://data.lacity.org/api/views/2nrs-mtv8/rows.csv?accessType=DOWNLOAD
#https://www.kaggle.com/datasets/zsinghrahulk/crypto-currency-bitcoin-and-ethereum-data/download?datasetVersionNumber=1
#

#create the DataFrame utilizing Pandas 
data = pd.read_csv("pandas/Crime_Data_from_2020_to_Present.csv") 
#data = pd.read_csv('pandas/ETH-BTC-USD.csv')
#data = pd.read_csv('pandas/Motor_Vehicle_Collisions.csv')

#data = data.iloc[0:-1 , [0,1,3,6]]
data = data.iloc[0:-1 , [1,5,12]]
#generate all info for this dataset
print(data.info())

print(data.describe())

