# pcost.py
#
# Exercise 1.27
totalcost = 0.0
with open('Downloads/portfolio.csv', 'rt') as f:
    headers = next(f)
    for line in f:
        row = line.split(',')
        shares = int(row[1])
        price = float(row[2])
        totalcost += shares * price
        
    print('Total cost', totalcost)
    
# Exercise 2.15
import csv
def portfolio_cost(filename):
    totalcost = 0.0
    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for rowno, row in enumerate(rows, start=1):
            try:
                shares = int(row[1])
                price = float(row[2])
                totalcost += shares * price
            except ValueError:
                print(f'Row {rowno}: Bad row: {row}')
    return total_cost
        
print('Total cost', totalcost)

cost = portfolio_cost('Downloads/missing.csv')





***
pandas
cborne.plot
