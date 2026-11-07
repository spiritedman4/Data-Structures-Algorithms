

test_cases = [([1,1,1],2),([1,2,3],3)]


'''
Below is the brute force method

Time Complexity: O(n^2) - Takes two loops
Space Complexity: O(1) - Does not use many variables even when the array will be larger

'''

def sub_arr_sum_equals_k(nums,k):
    n = len(nums)
    count = 0
    for start in range(n):
        total = 0
        for j in range(start,n):
            total+=nums[j]
            if total == k:
                count+=1
    return count


for test_case in test_cases:
    sub_arr_sum_equals_k(nums=test_case[0],k=test_case[1])