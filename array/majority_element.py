

test_arr = [[2,2,1,1,1,2,2,1,1],[3,2,3]]


'''
This is a brute force method uses a dict of O(n) time and O(n) space complexity.

'''
def find_majority_element(arr):
    element_state = {}
    arr_half_len = len(arr)//2
    max_occr_element = float('inf')
    for num in arr:
        element_state[num] = element_state.get(num,0) + 1
        if element_state[num] > arr_half_len:
            max_occr_element=num
    return max_occr_element


for arr in test_arr:
    majority_element = find_majority_element(arr=arr)
    print(f"Majority Element: {majority_element}")
