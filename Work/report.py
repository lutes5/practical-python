# report.py
#
# Exercise 2.4
import csv

def read_portfolio(filename):
    '''Computes the total cost (shares*price) of a portfolio file'''
    portfolio = []
    
    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            holding = (row[0], int(row[1]), float(row[2]))
            portfolio.append(holding)
    return portfolio

# Exercise 2.5
import csv

def read_portfolio(filename):
    '''Creates dictionary of a portfolio file'''
    portfolio = {}
    
    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            stock = {
                'name': row[0]
                'shares': int(row[1])
                'price': float(row[2]))
            }
            portfolio.append(stock)
    return portfolio

# Exercise 2.6 
import csv

def read_prices(filename):
    '''Reads stock prices and put into a dictionary'''
    stock_prices = {}
    
    with open(filename) as f:
        rows = csv.reader(f)
        for row in rows:
            try:
                stock_prices[row[0]] = float(row[1])
            except IndexError:
                pass
    return stock_prices
                
portfolio = read_portfolio('../../Work/Data/portfolio.csv')
stock_prices    = read_prices('../../Work/Data/prices.csv')

# Calculate the total cost of the portfolio
total_cost = 0.0
for s in portfolio:
    total_cost += s['shares']*s['price']

print('Total cost', total_cost)

# Compute the current value of the portfolio
total_value = 0.0
for s in portfolio:
    total_value += s['shares']*stock_prices[s['name']]

print('Current value', total_value)
print('Gain', total_value - total_cost)
