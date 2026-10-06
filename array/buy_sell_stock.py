
# get the max profit from the stock prices

test_arr = [[7,1,5,3,6,4],[7,6,4,3,1]]


'''
But the below method is O(n2) time complexity as it iterates over all the elements by two loops.
We have to solve this by O(n) but I tried this on my own to solve it.
'''
def get_max_profit(prices):
        max_profit = 0
        for i in range(len(prices)):
                buy = prices[i]
                for j in range(i+1,len(prices)-1):
                        profit = prices[j] - buy
                        if profit > buy and profit > max_profit:
                                max_profit = profit
        return max_profit
                
                        
                        
for prices in test_arr:
        max_profit = get_max_profit(prices=prices)
        print(f"Max profit:{max_profit}")