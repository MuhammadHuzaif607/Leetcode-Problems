prices = [7,1,5,3,6,4]
stock = prices[0]
max_profit = 0
for price in prices:
    if price < stock:
        stock = price
    curr_profit =  price - stock
    max_profit = max(max_profit,curr_profit) 
print(max_profit)


