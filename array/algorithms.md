
**Bubble Sort**

Bubble sort needs two loops, outer loop and the inner loop.
Outer loop is for to iterate through every elements and the inner loop is for comparing and swapping the adjacent elements.
For every outer loop, it will omit the last element because already it will be the sorted one and will have the maximum value, so no need of comparing it.


| Case | Time | Why |
|---|---|---|
| Best (sorted) | O(n) | early exit after 1 clean pass |
| Average | O(n²) | random disorder needs many passes |
| Worst (reverse sorted) | O(n²) | maximum swaps needed every pass |
| Space | O(1) | sorts in place, no extra structures |


**Two Pointer**

Two Pointer is nothing but using two variables in array to reverse it. Like start and stop variable.
we validate the start and stop in the loop until the two variables becomes same.




