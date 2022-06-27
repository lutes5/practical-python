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
    portfolio = []
    
    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            stock = {
                'name' : row[0],
                'shares' : int(row[1]),
                'price' : float(row[2])
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
                
portfolio = read_portfolio('Downloads/portfolio.csv')
prices = read_prices('Downloads/prices.csv')

# Calculate the total cost of the portfolio
total_cost = 0.0
for s in portfolio:
    total_cost += s['shares']*s['price']

print('Total cost', total_cost)

# Compute the current value of the portfolio
total_value = 0.0
for s in portfolio:
    total_value += s['shares']*prices[s['name']]

print('Current value', total_value)
print('Gain', total_value - total_cost)

# Exercise 2.9 

def make_report(portfolio, prices):
    '''
    Takes a list of stocks and dictionary of prices as input and returns
    a list of tuples
    '''
    rows = []
    for stock in portfolio:
        current_price = prices[stock['name']]
        change = current_price - stock['price']
        summary = (stock['name'], stock['shares'], current_price, change)
        rows.append(summary)
    return rows

report = make_report(portfolio, prices)
headers = ('Name', 'Shares', 'Price', 'Change')
'{:>10s} {:>10s} {:>10} {:>10s}'.format(headers)

for r in report:
    print('%10s %10d %10.2f %10.2f' % r)
    
    
