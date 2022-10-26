import yfinance as yf
import pandas as pd
import datetime
import numpy

start_date = datetime.datetime(1990,1,5)
start_date_next = datetime.datetime(1990,1,6)
end_date = datetime.datetime(2021,1,5)
end_date_next = datetime.datetime(2021,1,6)


company_tickers = open("s&p_data/constituents_symbols.txt", "r")

Symbols = company_tickers.read().splitlines()

# iterate over each symbol
# for i in Symbols:  
with open('s&p_data\constituents_performance.txt', 'w') as f:

    for i in Symbols:

        try:
            # Download the stock price 
            stock_start_data = yf.download(i,start=start_date, end=start_date_next, progress=False)
            stock_end_data = yf.download(i,start=end_date, end=end_date_next, progress=False)

            print("Data access successful")

            buy_price = stock_start_data['Open'][0]
            sell_price = stock_end_data['Open'][0]

            print(buy_price)
            print(sell_price)

            percent_gains = ((sell_price / buy_price) - 1) * 100

            print("Performance of " + i + " during period (excl. dividends):")
            print(stock_start_data)
            print(stock_end_data)

            print("Performance (as %): " + str(percent_gains))

            f.write(i + "," + str(percent_gains) + "\n")
            
        except Exception:
            print("Failed to gather performance for ticker " + i)
            f.write(i + ",None" +"\n")

        print("-----------------------------")


company_tickers.close()