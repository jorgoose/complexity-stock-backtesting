# Do Companies With Simpler 10-K Filings Outperform?
Testing the historical performance of company's stocks based on the inherent complexity of their 10-K report filed with the SEC.

The "complexity" score of each report was determined by a [Flesch-Kincaid readability](https://en.wikipedia.org/wiki/Flesch%E2%80%93Kincaid_readability_tests) scoring system.

Overview of Python scripts used for analysis:  
<br/>
*reportCollector.py* - Used to gather 10-K filings for each company  
*complexityAnalysis.py* - Used to calculate complexity score of each company based on their 10-K  
*performanceBacktest.py* - Used to calculate historical stock performance of each company  
*dataAndCorrelation.py* - Used to combine the two sets of data into a single file, and to calculate statistical correlation between the two variables  
*plotData.py* - Used to create graph for the resulting set of combined data (shown below)  



![alt text](https://raw.githubusercontent.com/jorgoose/complexity-stock-backtesting/main/10KResults.PNG)
