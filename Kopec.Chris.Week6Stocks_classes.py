"""
Author:           Chris Kopec
Date Created:     7/28/2021
Functionality:    This program calculates earnings/loss for the stock values provided and displays highest/lowest stock gain/loss

"""
# import modules
from datetime import date
from datetime import datetime
from os import read
import week4functions
import sqlite3
import json
import pygal

file_path = '/Users/chriskopec/Desktop/DenverUniversity/Class 5 - Python/AllStocks.json'
with open(file_path) as json_file:
    data_set = json.load(json_file)
for stock in data_set:
    print(stock['Symbol'], stock['Date'],
          stock['Open'], stock['High'],
          stock['Low'], stock['Close'],
          stock['Volume'])




# create a table 'investor.db'
conn = sqlite3.connect('investor.db')

# create a cursor
c = conn.cursor()







# create variable showing location of excel document to read
workspace = r'/Users/chriskopec/Desktop/DenverUniversity/Class 5 - Python'
stocksFile = workspace + '/' + 'Lesson6_Data_Stocks.csv'
bondsFile = workspace + '/' + 'Lesson6_Data_Bonds.csv'

# try catch statement for any errors that may occur in the future
try:
    read_file = open(stocksFile, 'r')
except:
    print('The file does not exist')

try:
    read2_file = open(bondsFile, 'r')
except:
    print('The file does not exist')


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
# *** not in use at the moment but will be used for writing to files in future release
    def print_investor_portfolio(self):
        print("\n | Stock ownership for " + self.firstName + "" + self.lastName + " | ID - " + str(self.investorID))
        print(" | Stock |\t" + " | Share |\t" + " | Purchase Price |\t" + "| Purchase Date |\t" + "| Purchase ID | \n")
        for stock in self.stock:
            print(" | " + stock.ticker + " |\t \t" + str(stock.shareQuantity) + "   |\t " + str(stock.purchasePrice) + "|\t\t" + str(stock.purchaseDate) + "|\t\t" + str(stock.purchaseID))
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


#contents = read_file.read()
contents = read_file.readline()
contents = contents.strip('\n')

contents2 = read2_file.readline()
contents2 = contents2.strip('\n')

# formats reading file into a list for index place holders
header2Split = contents2.split(',')
symbol_index2 = header2Split.index('SYMBOL')
noshares_index2 = header2Split.index('NO_SHARES')
purchprice_index2 = header2Split.index('PURCHASE_PRICE')
currentval_index2 = header2Split.index('CURRENT_VALUE')
purchdate_index2 = header2Split.index('PURCHASE_DATE')
coupon_index = header2Split.index('Coupon')
yield_index = header2Split.index('Yield')

# formats reading file into a list for index place holders
headerSplit = contents.split(',')
symbol_index = headerSplit.index('SYMBOL')
noshares_index = headerSplit.index('NO_SHARES')
purchprice_index = headerSplit.index('PURCHASE_PRICE')
currentval_index = headerSplit.index('CURRENT_VALUE')
purchdate_index = headerSplit.index('PURCHASE_DATE')
print(symbol_index, noshares_index, purchprice_index, currentval_index, purchdate_index)

# strips file of \n carriage return
stockList = []
for line in read_file:
    line_split = line.split(',')
    line_split[purchdate_index] = line_split[purchdate_index].strip('\n')

#    print(line_split[symbol_index], line_split[noshares_index], line_split[purchprice_index], line_split[currentval_index], line_split[purchdate_index])
    new_stock = Stock(line_split[symbol_index],
                      line_split[noshares_index],
                      line_split[purchdate_index],
                      line_split[currentval_index],
                      line_split[purchdate_index],
                      9999999)
    stockList.append(new_stock)
    investor_bob.stockAppend(line_split[symbol_index],
                      line_split[noshares_index],
                      line_split[purchdate_index],
                      line_split[currentval_index],
                      line_split[purchdate_index],
                      9999999)



for stock in stockList:
#    print(stock.ticker, stock.shareQuantity, stock.purchasePrice, stock.currentValue, stock.purchaseDate, stock.purchaseID, '009112221')
    newlist = []
    newlist = [stock.ticker, stock.shareQuantity, stock.purchasePrice, stock.currentValue, stock.purchaseDate, stock.purchaseID, investor_bob.investorID]
    
    c.execute("INSERT INTO stock VALUES %r" % tuple(newlist))


conn.commit()

conn.close()


# initiates output file write by openening file
outfile = workspace + '/' + 'stockoutfile.txt'
write_file = open(outfile, 'w')



# loops through reading file and assigns values to list
bondList = []
for line in read2_file:
    line_split = line.split(',')
    line_split[purchdate_index] = line_split[purchdate_index].strip('\n')


    new_bond = Bond(line_split[symbol_index2],
                      line_split[noshares_index2],
                      line_split[purchdate_index2],
                      line_split[currentval_index2],
                      line_split[purchdate_index2],
                      9999999,
                      line_split[coupon_index],
                      line_split[yield_index])
    bondList.append(new_bond)

"""        
# loops through stocks and bonds and writes them to the output file
for stock in stockList:
    write_file.write(stock.ticker + '\t' + stock.shareQuantity + '\t' + stock.purchasePrice + '\t' + stock.currentValue + '\t' + str(stock.purchaseDate) + '\t' + str(stock.purchaseID))
    print("Writing to file: " + stock.ticker + '\t' + stock.shareQuantity + '\t' + stock.purchasePrice + '\t' + stock.currentValue + '\t' + str(stock.purchaseDate) + '\t' + str(stock.purchaseID))
for bond in bondList:
    write_file.write(bond.ticker + '\t' + bond.shareQuantity + '\t' + bond.purchasePrice + '\t' + bond.currentValue +'\t' + str(bond.purchaseDate) + '\t' + str(bond.purchaseID) + '\t' + str(bond.coupon) + '\t' + str(bond.bondYield))
    print("Writing to file: " + bond.ticker + '\t' + bond.shareQuantity + '\t' + bond.purchasePrice + '\t' + bond.currentValue +'\t' + str(bond.purchaseDate) + '\t' + str(bond.purchaseID) + '\t' + str(bond.coupon) + '\t' + str(bond.bondYield))
"""


# gracefull close out file for reading and writing
write_file.close()
read_file.close()