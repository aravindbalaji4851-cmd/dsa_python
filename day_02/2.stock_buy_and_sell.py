prices = [9,6,5,3,7,4]

max_profit = 0

for i in range(0,len(prices)-1):

    for j in range(i+1,len(prices)):

        if prices[i] < prices[j]:

            profit = prices[j] - prices[i]

            if max_profit < profit : 

                max_profit = profit

print(max_profit)









