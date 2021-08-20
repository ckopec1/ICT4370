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

# gets live price using the yahoo_fin library calling the API
print("Today's Date: " + today.strftime("%m/%d/%y") + "\n" + ('-' * 25))
for stock in stockSymbol:
    liveprice = round(si.get_live_price(stock),2)
    print("Current Price: $" + str(liveprice))
    from2010 = si.get_data(stock, start_date = '01/01/2010')

# gets data from API
from2010googl = si.get_data('fb', start_date = '01/01/2010', index_as_date = False)
from2010msft = si.get_data('msft' , start_date = '01/01/2010', index_as_date = False)
from2010rds = si.get_data('rds-a' , start_date = '01/01/2010', index_as_date = False)
from2010aig = si.get_data('aig' , start_date = '01/01/2010', index_as_date = False)
from2010fb = si.get_data('fb' , start_date = '01/01/2010', index_as_date = False)

# maps data to plot
plt.plot(from2010googl['date'],from2010googl['close'])
plt.plot(from2010msft['date'],from2010msft['close'])
plt.plot(from2010rds['date'],from2010rds['close'])
plt.plot(from2010aig['date'],from2010aig['close'])
plt.plot(from2010fb['date'],from2010fb['close'])

# maps data to graph
plt.title('Prices from 2010 - Today')
plt.xlabel('Date')
plt.ylabel('Value')

# displays graph
plt.show()
