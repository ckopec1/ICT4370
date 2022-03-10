"""
Author:           Chris Kopec
Date Created:     8/5/2021
Functionality:    This program graphs stock prices relative to date
"""
# import modules
from datetime import datetime
import json
from typing import NewType
import matplotlib.pyplot as plt 
import matplotlib

# create class for stock and create objects
class Stock():
    """Relative stock information"""
    def __init__(self, ticker, date, close):
        self.ticker = ticker
        self.datelist = []
        self.closelist = []

    def appendClosePrice(self, close, date):
        self.closelist.append(close)
        self.datelist.append(date)
    
# sets file variable
file_path = '/Users/chriskopec/Desktop/DenverUniversity/Class 5 - Python/AllStocks.json'
try:
    with open(file_path) as json_file:
        all_data = json.load(json_file)
except:
    print('File not found')

# creates dictionary for matplotlib to graph
stockDict = {}
for line in all_data:
    if line['Symbol'] not in stockDict:
        newstock = Stock(line['Symbol'], line['Close'], line['Date'])
        print("Stock: ", line['Symbol'])
        stockDict[line['Symbol']] = {'Stock': newstock}
    stockDict[line['Symbol']]['Stock'].appendClosePrice(line['Close'],datetime.strptime(line['Date'], '%d-%b-%y'))

# formats plt data for graphing
for stock in stockDict:
    print('Stock: ', stock)
    close = stockDict[stock]['Stock'].closelist
    dates = matplotlib.dates.date2num(stockDict[stock]['Stock'].datelist)
    name = stockDict[stock]['Stock'].ticker
    plt.plot_date(dates, close, linestyle='solid', label = name)

# calls plt from matplotlib library for graphing
plt.legend()
plt.show()


