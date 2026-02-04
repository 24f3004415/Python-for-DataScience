prices = [7,2,1,5,6,4,8]

min_price = float('inf')
profit = 0

for i in range(len(prices)):
    if prices[i] < min_price:
        min_price = prices[i]
    
    if prices[i] > min_price:
        profit = prices[i] - min_price