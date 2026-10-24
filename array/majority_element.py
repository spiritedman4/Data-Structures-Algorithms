

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



'''

For a better method using O(n) we can use Boyer-Moore's Voting Algorithm.

Boyer-Moore's voting algo is kind of cancelling out the occurences. Each occurence of the
current element is a vote for and if not vote against. So the majority element can't be fully
cancelled out and it will be always more than all of them combined

'''


def find_majority_element_bmva(nums):
    count = 0
    candidate = None
    for num in nums:
        if count==0:
            candidate = num
            count+=1
        elif candidate == num:
            count+=1
        else:
            count-=1
    return candidate if nums.count(candidate) > len(nums)//2 else None

for arr in test_arr:
    majority_element=find_majority_element_bmva(arr)
    print(f"Majority Element by Moore's Voting Algorithm: {majority_element}")

