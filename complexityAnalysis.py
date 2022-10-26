from pyexpat import features
import textstat
from bs4 import BeautifulSoup
import os
import textstat
import csv



# Iterate over files in directory, find HTML document, and assign file path to variable
def findFiles(directory):
    for filename in os.listdir(directory):
        f = os.path.join(directory, filename)

        # Check if "f" is the report file we want: if so, return the file path, otherwise keep looking for the file
        if os.path.isfile(f):
            if filename.endswith('.html'):
                return f
        else:
            return findFiles(f)

# TODO Cycle through file of S&P 500 tickers, and for each company:
company_tickers = open("s&p_data/constituents_symbols.txt")

with open('s&p_data\constituents_complexity.txt', 'w') as f:
    for ticker in company_tickers:
            try:
                ticker = ticker.rstrip()

                # Call findFiles() on start_directory. Function starts with base directory and recursively searches for HTML file.
                # Assign directory and initialize file path for 10-K document
                start_directory = "reports/sec-edgar-filings/" + ticker

                file_path = findFiles(start_directory)

                # Open file based on file path to read contents
                page = open(file_path, encoding="utf8")
                soup = BeautifulSoup(page.read(), features="xml")

                # Get raw text from opened HTML file of 10-K and assign to variable
                raw_text = soup.get_text()

                # Print text complexity score based on raw text
                print(ticker)
                complexityValue = textstat.flesch_reading_ease(raw_text)
                print(complexityValue)
                f.write(ticker + "," + str(complexityValue) + "\n")
            except:
                print("Error accessing company 10-K for " + ticker + ". File most likely missing from target directory.")
                f.write(ticker + "," + "null\n")

company_tickers.close()
