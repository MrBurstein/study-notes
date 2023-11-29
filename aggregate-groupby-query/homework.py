import pandas as pd
import os
#https://www.kaggle.com/datasets/zsinghrahulk/crypto-currency-bitcoin-and-ethereum-data/download?datasetVersionNumber=1
data = pd.read_csv('pandas/ETH-BTC-USD.csv')

import pandas as pd

bitcoin_df = data[data['Currency'] == 'Bitcoin']

ethereum_df = data[data['Currency'] == 'Etherium']


import matplotlib.pyplot as plt
# Plotting Bitcoin and Ethereum opening and closing prices over time
plt.figure(figsize=(12, 6))

# Bitcoin prices
plt.plot(bitcoin_df['Date'], bitcoin_df['Open'], label='Bitcoin Open', color='orange')
plt.plot(bitcoin_df['Date'], bitcoin_df['Close'], label='Bitcoin Close', color='blue')

# Ethereum prices
plt.plot(ethereum_df['Date'], ethereum_df['Open'], label='Ethereum Open', color='green')
plt.plot(ethereum_df['Date'], ethereum_df['Close'], label='Ethereum Close', color='red')

# Adding labels and title
plt.xlabel('Date')
plt.ylabel('Price')
plt.title('Bitcoin and Ethereum Prices Over Time')
plt.legend()
plt.xticks(rotation=45)  # Rotate x-axis labels for better readability

# Show the plot
plt.tight_layout()
plt.savefig('aggregate-groupby-query/price_chart.jpg')


# Calculating percentage change in closing prices for Bitcoin and Ethereum
bitcoin_first_date = bitcoin_df.iloc[0]['Date']
ethereum_first_date = ethereum_df.iloc[0]['Date']

bitcoin_df['BTC_Percentage_Change'] = (bitcoin_df['Close'] - bitcoin_df.loc[bitcoin_df['Date'] == bitcoin_first_date, 'Close'].iloc[0]) / bitcoin_df.loc[bitcoin_df['Date'] == bitcoin_first_date, 'Close'].iloc[0] * 100
ethereum_df['ETH_Percentage_Change'] = (ethereum_df['Close'] - ethereum_df.loc[ethereum_df['Date'] == ethereum_first_date, 'Close'].iloc[0]) / ethereum_df.loc[ethereum_df['Date'] == ethereum_first_date, 'Close'].iloc[0] * 100

# Plotting percentage change over time for Bitcoin and Ethereum
plt.figure(figsize=(12, 6))

plt.plot(bitcoin_df['Date'], bitcoin_df['BTC_Percentage_Change'], label='BTC Percentage Change', color='orange')
plt.plot(ethereum_df['Date'], ethereum_df['ETH_Percentage_Change'], label='ETH Percentage Change', color='blue')

plt.xlabel('Date')
plt.ylabel('Percentage Change')
plt.title('Percentage Change in Closing Prices Over Time (BTC vs ETH)')
plt.legend()
plt.xticks(rotation=45)

plt.tight_layout()
plt.show()
plt.savefig('aggregate-groupby-query/price_chart_over_time.jpg')
