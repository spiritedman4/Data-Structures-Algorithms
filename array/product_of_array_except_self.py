 
test_arrs =[[1,2,3,4],[-1,1,0,-3,3]]



'''
The below solution is solved by brute force using Division Approach.
'''

def product_of_array_except_self(nums):
    non_zeros_product = 1
    zeros_count = 0

    for i in nums:
        if i ==0:
            zeros_count+=1
        else:
            non_zeros_product*=i

    result = [0] * len(nums)
    if zeros_count==0:
        for idx,num in enumerate(nums):
            result[idx] = non_zeros_product // num
    elif zeros_count ==1:
        zero_index = nums.index(0)
        result[zero_index] = non_zeros_product

    return result

    

for arr in test_arrs:
    result = product_of_array_except_self(arr)
    print(f"The product of array except self: {result}")


'''
 The below method is an optmized approach too, straight forward way.
 It does not use division.
 This uses two extra arrays so O(n)

'''

def product_of_array_except_self_opt1(nums):
    product = 1
    arr_len = len(nums)
    left_product,right_product,result = [1] * arr_len,[1] * arr_len,[1] * arr_len
    for i in range(arr_len):
        left_product[i] = product = product * nums[i]
    
    product = 1
    for i in range(arr_len-1,-1 ,-1):
        right_product[i] = product = product * nums[i]
    result[0] = right_product[1]
    result[arr_len-1] =left_product[arr_len-2]

    for i in range(1,arr_len-1):
        result[i] = left_product[i-1] * right_product[i+1]

    return result            

            


for arr in test_arrs:
    result = product_of_array_except_self_opt1(arr)
    print(f"The product of array except self: {result}")
