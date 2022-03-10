"""
Author:           Chris Kopec
Date Created:     8/15/2021
Functionality:    This program calculates earnings/loss for the stock values provided and displays highest/lowest stock gain/loss

"""
import unittest


# assigns values to lists accordingly
stockSymbol = ['GOOGLE', 'MSFT', 'RDS-A', 'AIG', 'FB']
numShares = [25, 85, 400, 235, 130]
purchPrice = [772.88, 56.60, 49.58, 54.21, 124.31]
currValue = [941.53, 73.04, 55.74, 65.27, 175.45]
earnLossList = []
stockIncrease = 0
a = 0

# calculates and prints output in a for loop looping through the lists
print('\n Stock ownership for Bob Smith')
print('\t' + 'Stock' + '\t\t# of Shares' + '\tEarnings/Loss')
for stock in range(len(stockSymbol)):
    initialInvestment = numShares[stock] * purchPrice[stock]
    currentInvestment = numShares[stock] * currValue[stock]
    earnLoss = currentInvestment - initialInvestment
    earnLossList.append(earnLoss)
    print(stockSymbol[stock], numShares[stock], round(earnLoss,2))

# checks which number is greatest to find the greatest gain for the portfolio value. If earnings are 
# less than zero, then it will find the lowest number using the sort function
if earnLoss > 0:
    for num in earnLossList:
        if num > a:
            a = num 
elif earnLoss < 0:
    earnLossList.sort()
    a = earnLossList[:1]

# finds the index of the greatest increase and aligns it to the stock symbol to display properly.
# however, number must exist in the list
index = earnLossList.index(a)
if earnLoss > 0:
    print('The stock with the highest increase in value in your portfolio on a per-share basis is: ' + stockSymbol[index])
elif earnLoss < 0:
    print('The stock with least decrease in value in your portfolio on a per-share basis is: ' + stockSymbol[index])