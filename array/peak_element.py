
## find pick element in an array

test_arr = [[1,2,3,1], [1,2,1,3,5,6,4]]

def find_pick_element(arr):
        n = len(arr)
        if n == 0:
             return -1
        max_element = arr[0]
        max_element_idx=0
        for i in range(1,n):
            if arr[i] > max_element:
                max_element = arr[i]
                max_element_idx = i
        print(f'Peak Element: {max_element}')
        return max_element_idx

for arr in test_arr:
    find_pick_element(arr)



