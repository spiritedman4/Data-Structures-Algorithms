import time
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
                for j in range(i+1,len(prices)):
                        profit = prices[j] - buy
                        if profit > buy and profit > max_profit:
                                max_profit = profit
        return max_profit
                

        
                        
for prices in test_arr:
        start_time = time.perf_counter()
        max_profit = get_max_profit(prices=prices)
        end_time = time.perf_counter()
        elapsed_time = end_time - start_time
        print(f"Elapsed time for O(n2) operation: {elapsed_time*1000:.6f} ms")
        print(f"Max profit:{max_profit}")


def get_max_profit_on(prices):
	min_price = float('inf')
	max_profit = 0
    
	for price in prices:        
		if price < min_price:
			min_price = price
		elif price - min_price > max_profit:
			max_profit = price - min_price

	return max_profit

                


for prices in test_arr:
        start_time = time.perf_counter()
        max_profit = get_max_profit_on(prices=prices)
        end_time = time.perf_counter()
        elapsed_time = end_time - start_time
        print(f"Elapsed time for O(n) operation: {elapsed_time * 1000:.6f} ms")
        print(f"Max profit:{max_profit}")
