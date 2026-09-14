from collections import deque

#insertion at the beginning

my_list = [1,2,3,4,5]
print(my_list)

# This is O(n) as it will swap all the other elements
my_list.insert(0,6) 
print(my_list)


##looping throug array

for i in range(1,11):
    print(i)




reversed= my_list.reverse()
print(reversed)



for i in  range(len(my_list) -1 , -1 , -1):
    print('array reverse' , my_list[i])