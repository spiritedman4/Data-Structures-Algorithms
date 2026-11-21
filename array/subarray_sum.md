
### Subarray sum

A prefix sum represents the cumulative sum of elements up to a particular index.

take an array [1, 2, 3, 4, 5] 

before 1** **there is no value so we can consider it as 0

cumulative sum is = [1 , 3, 6, 10, 15]

**To calculate the sum of particular sub arrays we can use prefix sum.
For e.g:
    for the sub array in the above [3,4] we can use the below formula
     
    sum(i,j) = prefixSum(j) - prefixsum(1-1)

    we eliminate the elements before the sub array.

    we can move the formula into further

    k = prefixSum(j) - prefixsum(1-1)

    prefixsum(1-1) = prefixSum(j) - k

**


