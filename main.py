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
else:
    print("INVALID SELECTION!!")
    

    

# Set the ticker symbol and the start and end dates for the analysis
start_date = str(input("Enter the start date:(year-month-date)"))
end_date= str(input("Enter the ending date:(year-month-date)"))

# Get the stock data from Yahoo Finance
stock_data = yf.download(symbol, start=start_date, end=end_date)

# Calculate the 50-day moving average
stock_data['MA50'] = stock_data['Adj Close'].rolling(window=50).mean()
# Calculate the 10-day moving average
stock_data['MA10'] = stock_data['Adj Close'].rolling(window=10).mean()
# Calculate the 20-day moving average
stock_data['MA20'] = stock_data['Adj Close'].rolling(window=20).mean()
# Calculate the 100-day moving average
stock_data['MA100'] = stock_data['Adj Close'].rolling(window=100).mean()

# Print the stock data
print(stock_data.tail())

# Plot the stock data with the 50-day and 200-day moving averages
import matplotlib.pyplot as plt
plt.plot(stock_data['Adj Close'], label='Adj Close')
plt.plot(stock_data['MA10'], label='MA10')
plt.plot(stock_data['MA20'], label='MA20')
plt.plot(stock_data['MA50'], label='MA50')
plt.plot(stock_data['MA100'], label='MA100')
plt.legend(loc='upper left')
plt.show()
