prices = [15, 10, 50, 1, 12, 20]
# prices = [7, 6, 5, 4, 1]
# max_profit = 0
# for i in range(0, len(prices)):
#     min_price = prices[i] #1
#     for j in range(i+1, len(prices)):
#         if prices[j] > min_price: 
#             avg_price = prices[j] - min_price  #40
#             if avg_price > max_profit:
#                 max_profit = avg_price   #40
# print(max_profit) 

cost_price = prices[0]
max_profit = 0
for current_price in prices:
    cost_price = min(cost_price, current_price)
    max_profit = max(max_profit, current_price-cost_price)
print(max_profit)    