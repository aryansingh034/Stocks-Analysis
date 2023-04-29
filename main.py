import yfinance as yf
print("Select the stock for analysis:")
print("1.AMZN\n 2.TSLA\n 3.INTC\n 4.AAPL\n 5.F\n 6.AMD\n 7.META\n 8.NVDA\n 9.GOOGL\n 10.MSFT\n 11.CSCO\n 12.BABA\n 13.WBD\n 14.LYD\n 15.JPM")
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
elif a==6:
    symbol="AMD"
elif a==7:
    symbol="META"
elif a==8:
    symbol="NVDA"
elif a==9:
    symbol="GOOGL"
elif a==10:
    symbol="MSFT"
elif a==11:
    symbol="CSCO"
elif a==12:
    symbol="BABA"
elif a==13:
    symbol="WBD"
elif a==14:
    symbol="LYD"
elif a==15:
    symbol="JPM"

    

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
