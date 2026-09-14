
## Reverse an array using two pointer approach

new_array = [52,62,72,83,95]


def reverse_array(start, stop):
    global new_array
    while (stop > start):
        temp = new_array[start]
        new_array[start] = new_array[stop]
        new_array[stop] = temp
        start+=1
        stop-=1

print('Array before reverse:', *new_array)
reverse_array(0,len(new_array)-1)
print('Array after reverse:', *new_array)


## we can use array in python

from array import array

arr1 = array('i' , [1,2,4,4,5])
print(arr1)