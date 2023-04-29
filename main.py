import yfinance as yf
print("Select the stock for analysis:")
print("1.AMZN\n 2.TSLA\n 3.INTC\n 4.AAPL\n 5.F")
a=int(input("Select the stock for analysis:"))
if a==1:
    symbol="AMZN"
elif a==2:
    symbol="TSLA"
elif a==3:
    symbol="INTC"
elif a==4:
    symbol="AAPL"
elif a==5:
    symbol="F"
    

# Set the ticker symbol and the start and end dates for the analysis
start_date = '2010-01-01'
end_date = '2022-04-29'

# Get the stock data from Yahoo Finance
stock_data = yf.download(symbol, start=start_date, end=end_date)

# Calculate the 50-day moving average
stock_data['MA50'] = stock_data['Adj Close'].rolling(window=50).mean()

# Calculate the 200-day moving average
stock_data['MA200'] = stock_data['Adj Close'].rolling(window=200).mean()

# Print the stock data
print(stock_data.tail())

# Plot the stock data with the 50-day and 200-day moving averages
import matplotlib.pyplot as plt
plt.plot(stock_data['Adj Close'], label='Adj Close')
plt.plot(stock_data['MA50'], label='MA50')
plt.plot(stock_data['MA200'], label='MA200')
plt.legend(loc='upper left')
plt.show()
