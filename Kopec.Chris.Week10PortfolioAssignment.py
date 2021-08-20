"""
Author: Chris Kopec
Date: 8/21/2021
Description: Using yahoo_fin API to get real-time stock data and graph it through matplotlib
"""

import yahoo_fin.stock_info as si
import matplotlib.pyplot as plt
from datetime import date

# stocks to be observed and graphed
stockSymbol = ['GOOGL', 'MSFT', 'RDS-A', 'AIG', 'FB']        

# get input from user and appends it to the list to graph in addition to the above tickers
stockinput = input("Enter the stock you would like to graph:")
stockSymbol.append(stockinput)

# gets live price using the yahoo_fin library calling the API
today = date.today()
print("Today's Date: " + today.strftime("%m/%d/%y") + "\n" + ('-' * 25))
for stock in stockSymbol:
    liveprice = round(si.get_live_price(stock),2)
    print("Current Price: $" + str(liveprice))
    from2010 = si.get_data(stock, start_date = '01/01/2010', index_as_date = False)
    plt.plot(from2010['date'],from2010['close'])

# maps data to graph
plt.title('Prices from 2010 - Today')
plt.xlabel('Date')
plt.ylabel('Value')

# displays graph
plt.show()
