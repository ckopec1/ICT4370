"""
Author:           Chris Kopec
Date Created:     6/27/2021
Functionality:    This program calculates earnings/loss for the stock values provided and displays highest/lowest stock gain/loss

"""

# creates dictionary with correct values
stockDictionary = {'GOOGL': {'shareQuantity': 25, 'purchasePrice': 772.88, 'currentValue': 941.53, 'purchaseDate': '8/1/2018'}}
stockDictionary['MSFT'] = {'shareQuantity': 85, 'purchasePrice': 56.60, 'currentValue': 73.04, 'purchaseDate': '8/1/2018'}
stockDictionary['RDS-A'] = {'shareQuantity': 400, 'purchasePrice': 49.58, 'currentValue': 55.74, 'purchaseDate': '8/1/2018'}
stockDictionary['AIG'] = {'shareQuantity': 235, 'purchasePrice': 54.21, 'currentValue': 65.27, 'purchaseDate': '8/1/2018'}
stockDictionary['FB'] = {'shareQuantity': 130, 'purchasePrice': 124.31, 'currentValue': 175.45, 'purchaseDate': '8/1/2018'}
stockDictionary['M'] = {'shareQuantity': 425, 'purchasePrice': 30.30, 'currentValue': 23.98, 'purchaseDate': '1/10/2018'}
stockDictionary['F'] = {'shareQuantity': 85, 'purchasePrice': 12.58, 'currentValue': 10.95, 'purchaseDate': '2/17/2018'}
stockDictionary['IBM'] = {'shareQuantity': 80, 'purchasePrice': 150.37, 'currentValue': 145.30, 'purchaseDate': '5/12/2018'}

# loops through the dictionary while calculating each individual stock value to display in the table
print("\n")
val = float('-inf')
highestIncrease = ""
print('\n Stock ownership for Bob Smith')
print('\t' + 'Stock' + '\t\t# of Shares' + '\tEarnings/Loss')
for key in stockDictionary:
    initialAmount = stockDictionary[key]['shareQuantity'] * stockDictionary[key]['purchasePrice']
    currentAmount = stockDictionary[key]['shareQuantity'] * stockDictionary[key]['currentValue']
    profit = currentAmount - initialAmount
    earnPerStock = profit / stockDictionary[key]['shareQuantity']
    profitRound = format(profit,".2f")
    print('\t' + key + '\t\t' + str(stockDictionary[key]['shareQuantity']) + '\t\t $' + str(profitRound))

# determines the highest value in the earnings per share value
    if earnPerStock > val:
        val = earnPerStock
        highestIncrease = key

# displays the highest earnings per share value if it is a gain - if loss, then displays otherwise
if earnPerStock >= 0:
    print('The stock with the highest increase in value in your portfolio on a per-share basis is: ' + str(highestIncrease))
elif earnPerStock < 0:
    print('The stock with least decrease in value in your portfolio on a per-share basis is: ' + str(highestIncrease))


