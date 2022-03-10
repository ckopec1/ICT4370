"""
Author:           Chris Kopec
Date Created:     7/14/2021
Functionality:    This program calculates earnings/loss for the stock values provided and displays highest/lowest stock gain/loss

"""
# import modules
from datetime import date
from datetime import datetime
import week4functions
import datetime

# create investor class and add objects
class Investor():
    """An investor's account information"""
    def __init__(self, firstName, lastName, address, phoneNum, investorID):
        self.firstName = firstName
        self.lastName = lastName
        self.address = address
        self.phoneNum = phoneNum
        self.investorID = investorID
        self.stock = []
        self.bond = []

# create method to append to stock or bond
    def stockAppend(self, ticker, shareQuantity, purchasePrice, currentValue, purchaseDate, purchaseID):
        self.stock.append(Stock(ticker, shareQuantity, purchasePrice, currentValue, purchaseDate, purchaseID))
    def bondAppend(self, ticker, shareQuantity, purchasePrice, currentValue, purchaseDate, purchaseID, coupon, bondYield):
        self.bond.append(Bond(ticker, shareQuantity, purchasePrice, currentValue, purchaseDate, purchaseID, coupon, bondYield))

    def printReport(self):
        for stock in self.stock:
            print(self.stock)


# create method to print final portfolio
    def print_investor_portfolio(self):
        print("\n | Stock ownership for " + self.firstName + "" + self.lastName + " | ID - " + str(self.investorID))
        print(" | Stock  " + " | Share |" + " Purchase Price" + " | Purchase Date" + " | Purchase ID | ")
        for stock in self.stock:
            print(stock)
        for bond in self.bond:
            print(" | " + bond.ticker + " | " + bond.shareQuantity + "   | " + bond.purchasePrice + "         | " + bond.purchaseDate + "      | " + bond.purchaseID + "           | ")

# create class for stock and create objects
class Stock():
    """Relative stock information"""
    def __init__(self, ticker, shareQuantity, purchasePrice, currentValue, purchaseDate, purchaseID):
        self.ticker = ticker
        self.shareQuantity = shareQuantity
        self.purchasePrice = purchasePrice
        self.currentValue = currentValue
        self.purchaseDate = purchaseDate
        self.purchaseID = purchaseID
    
# create class for stock and create objects
class Bond(Stock):
    """Relative bond information"""
    def __init__(self, ticker, shareQuantity, purchasePrice, currentValue, purchaseDate, purchaseID, coupon, bondYield):
        super().__init__(ticker,shareQuantity, purchasePrice, currentValue, purchaseDate, purchaseID)
        self.coupon = coupon
        self.bondYield = bondYield






    

# instantiate class and fill Bob Smith's information into the object
investor_bob = Investor('Bob', 'Smith', '511 N Smith Street', '630-990-0099', '009112221')
investor_bob.bondAppend(ticker = 'GT2:GOV', shareQuantity = '200', purchasePrice = '100.02',
 currentValue='100.05', purchaseDate='8/1/2017', purchaseID='1', coupon='1.38', bondYield='1.35%')

investor_bob.stockAppend('GOOGL', 25, 772.88, 941.53, '2018-8-1', 9889)
investor_bob.stockAppend('MSFT', 85, 56.60, 73.04, '2018-8-1', 3223)
investor_bob.stockAppend('RDS-A', 400, 49.58, 55.74, '2018-8-1', 3995)
investor_bob.stockAppend('AIG', 235, 54.21, 65.27, '2018-8-1', 2008)
investor_bob.stockAppend('FB', 130, 124.31, 175.45, '2018-8-1', 8332)
investor_bob.stockAppend('M', 425, 30.30, 23.98, '2018-8-1', 1952)
investor_bob.stockAppend('F', 85, 12.58, 10.95, '2018/2/17', 2885)
investor_bob.stockAppend('IBM', 80, 150.37, 145.30, '2018/12/5', 6816)




# call print class to print Bob's portfolio information
investor_bob.print_investor_portfolio()

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
#rint('\n Stock ownership for Bob Smith')
#print('\t' + 'Stock' + '\t\t# of Shares' + '\tEarnings/Loss' + '\t' + 'Yearly/Earning/Loss')
for key in stockDictionary:
    initialAmount = stockDictionary[key]['shareQuantity'] * stockDictionary[key]['purchasePrice']
    currentAmount = stockDictionary[key]['shareQuantity'] * stockDictionary[key]['currentValue']
    profit = currentAmount - initialAmount
    earnPerStock = profit / stockDictionary[key]['shareQuantity']
    profitRound = format(profit,".2f")
#    print('\t' + key + '\t\t' + str(stockDictionary[key]['shareQuantity']) + "\t\t$" +
#     "%5.2f" % week4functions.lossGain(stockDictionary[key]['shareQuantity'], stockDictionary[key]['purchasePrice'], stockDictionary[key]['currentValue']) + 
#     "\t" + "%5.2f" % week4functions.shareYieldPercent(stockDictionary[key]['purchasePrice'], stockDictionary[key]['currentValue']) + "%")

# determines the highest value in the earnings per share value
    if earnPerStock > val:
        val = earnPerStock
        highestIncrease = key

# displays the highest earnings per share value if it is a gain - if loss, then displays otherwise
#if earnPerStock >= 0:
#    print('The stock with the highest increase in value in your portfolio on a per-share basis is: ' + str(highestIncrease))
#elif earnPerStock < 0:
#    print('The stock with least decrease in value in your portfolio on a per-share basis is: ' + str(highestIncrease))


# creates dictionary with correct values

