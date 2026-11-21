

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


def sub_arr_equals_k_opt(nums,k):

    prefix_map = {0:1}
    prefix_sum = 0
    count = 0

    for num in nums:
        prefix_sum += num
        previous_prefix = prefix_sum - k

        if previous_prefix in prefix_map:
           count += prefix_map[prefix_sum]

        prefix_map[previous_prefix] = prefix_map.get(previous_prefix,0) + 1
    print(prefix_map)
    return count



for test_case in test_cases:
    count = sub_arr_equals_k_opt(nums=test_case[0], k=test_case[1])
    print(f'The count of sub array sum equals to {test_case[1]} is {count}')