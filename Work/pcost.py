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
