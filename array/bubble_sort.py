##sort using bubble sort

test_arr = [1,2,4,3,7,5,6,8,150,100]


def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(n-i-1):
            if test_arr[j] > test_arr[j+1]:
                test_arr[j+1], test_arr[j] = test_arr[j], test_arr[j+1]
                swapped =True
        if not swapped:
            print('Already sorted')
            break
    print('Sorted Array: ' , test_arr)

bubble_sort(test_arr)

            
