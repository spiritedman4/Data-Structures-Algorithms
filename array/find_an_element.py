
arr1= [1, 2, 3, 4] 

def find_an_element(element):
    for i in range(0,len(arr1)-1):
        if arr1[i] == element:
            return i
    return -1

for element in [1,3,5,7,6]:
    found = find_an_element(element=element)
    print(f'{element} Not Found') if found == -1 else print(f'{element} Found')