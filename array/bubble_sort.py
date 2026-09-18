##sort using bubble sort

test_arrs = [[1,2,4,3,7,5,6,8,150,100],[4,3,1,2,8,5,7],[1, 2, 3, 4, 5],[5, 4, 3, 2, 1],[3, 1, 3, 2, 1]]


def bubble_sort(arr):
    n = len(arr)
    passes = 0
    for i in range(n):
        passes+=1
        swapped = False
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j+1], arr[j] = arr[j], arr[j+1]
                swapped =True
        if not swapped:
            print('Already sorted')
            break
    print('Total Passes: ' , passes)
    print('Sorted Array: ' , arr)


for arr in test_arrs:
    bubble_sort(arr=arr)

            
