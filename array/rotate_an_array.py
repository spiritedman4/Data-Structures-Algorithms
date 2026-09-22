


'''
Array Rotation to the right by K Steps.
    1.K has to checked by modulo, as k should not be greater than the array size.
    2. As insertion at the start for the array is expensive, we can swap the elements by two pointer method.
    3. First reverse the whole array.
    4. Then Reverse the needed items that are in left side of the array from 0 to k -1 indexes.
    5. Then revert back the reversed right side elements in the array to its original posistion from k to len(arr)-1 index.

'''

class ArrayRotate:
    def reverse_arr(self,arr,start,stop):
        while start < stop:
            temp = arr[start]
            arr[start] = arr[stop]
            arr[stop] = temp
            start+=1
            stop-=1
        return arr

    def rotate_the_array(self,arr,k):
        k%=len(arr)
        reversed = self.reverse_arr(arr, 0, len(arr)-1)
        reversed = self.reverse_arr(reversed, 0 , k-1)
        reversed = self.reverse_arr(reversed,k, len(arr)-1)
        return reversed

arr_rotate = ArrayRotate()

test_arr = [[[-1,-100,3,99],2],[[1,2,3,4,5,6,7],3]]

for items in test_arr:
    arr,k = items
    reversed = arr_rotate.rotate_the_array(arr=arr,k=k)
    print(f"Rotated array by {k}:",reversed)