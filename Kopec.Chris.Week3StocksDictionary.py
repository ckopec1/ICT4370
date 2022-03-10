"""
Author:           Chris Kopec
Date Created:     7/11/2021
Functionality:    This program calculates earnings/loss for the stock values provided and displays highest/lowest stock gain/loss

"""
# import modules
from datetime import date
from datetime import datetime
import week4functions
import datetime

# creates dictionary with correct values
stockDictionary = {'GOOGL': {'shareQuantity': 25, 'purchasePrice': 772.88, 'currentValue': 941.53, 'purchaseDate': '2018-8-1'}}
stockDictionary['MSFT'] = {'shareQuantity': 85, 'purchasePrice': 56.60, 'currentValue': 73.04, 'purchaseDate': '2018-8-1'}
stockDictionary['RDS-A'] = {'shareQuantity': 400, 'purchasePrice': 49.58, 'currentValue': 55.74, 'purchaseDate': '2018-8-1'}
stockDictionary['AIG'] = {'shareQuantity': 235, 'purchasePrice': 54.21, 'currentValue': 65.27, 'purchaseDate': '2018-8-1'}
stockDictionary['FB'] = {'shareQuantity': 130, 'purchasePrice': 124.31, 'currentValue': 175.45, 'purchaseDate': '2018-8-1'}
stockDictionary['M'] = {'shareQuantity': 425, 'purchasePrice': 30.30, 'currentValue': 23.98, 'purchaseDate': '2018/10/1'}
stockDictionary['F'] = {'shareQuantity': 85, 'purchasePrice': 12.58, 'currentValue': 10.95, 'purchaseDate': '2018/2/17'}
stockDictionary['IBM'] = {'shareQuantity': 80, 'purchasePrice': 150.37, 'currentValue': 145.30, 'purchaseDate': '2018/12/5'}

# gets today's date
today = date.today()
todayDate = today.strftime("%Y-%m-%d")

# loops through the dictionary while calculating each individual stock value to display in the table
print("\n")
val = float('-inf')
highestIncrease = ""
print('\n Stock ownership for Bob Smith')
print('\t' + 'Stock' + '\t\t# of Shares' + '\tEarnings/Loss' + '\t' + 'Yearly/Earning/Loss')
for key in stockDictionary:
    initialAmount = stockDictionary[key]['shareQuantity'] * stockDictionary[key]['purchasePrice']
    currentAmount = stockDictionary[key]['shareQuantity'] * stockDictionary[key]['currentValue']
    profit = currentAmount - initialAmount
    earnPerStock = profit / stockDictionary[key]['shareQuantity']
    profitRound = format(profit,".2f")
    print('\t' + key + '\t\t' + str(stockDictionary[key]['shareQuantity']) + "\t\t$" +
     "%5.2f" % week4functions.lossGain(stockDictionary[key]['shareQuantity'], stockDictionary[key]['purchasePrice'], stockDictionary[key]['currentValue']) + 
     "\t" + "%5.2f" % week4functions.shareYieldPercent(stockDictionary[key]['purchasePrice'], stockDictionary[key]['currentValue']) + "%")

# determines the highest value in the earnings per share value
    if earnPerStock > val:
        val = earnPerStock
        highestIncrease = key

# displays the highest earnings per share value if it is a gain - if loss, then displays otherwise
if earnPerStock >= 0:
    print('The stock with the highest increase in value in your portfolio on a per-share basis is: ' + str(highestIncrease))
elif earnPerStock < 0:
    print('The stock with least decrease in value in your portfolio on a per-share basis is: ' + str(highestIncrease))


