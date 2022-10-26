from sec_edgar_downloader import Downloader
from bs4 import BeautifulSoup
import os

# TODO Cycle through file of S&P 500 tickers, and for each company:
company_tickers = open("s&p_data/constituents_symbols.txt")

for ticker in company_tickers:
    try:
        dl = Downloader("reports")

        # Get the latest 10-K filing for given company
        dl.get("10-K", ticker, amount=1)

        # Print notice for successful download of document
        print("Gathered document for " + ticker)

    except:
         print("Problem gathering 10-K for ticker " + ticker)

company_tickers.close()


