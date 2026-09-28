

'''
The first condition is for checking if the character is digit, it goes to else block and check for the num length 
and append it to the result, so the consecutive numbers also gets appended as one like 56,46.
Final condition if the digits are at the end it will be missed after the second condition(char check) as the number blocks are added
in else condtion to the array as a block.

'''


def extract_integer(s: str):

    result = []
    nums = ""
    for ch in s:
        if ch.isdigit():
            nums+=ch
        else:
            if len(nums)>0:
                result.append(nums)
                nums=''
    if len(nums)>0:
        result.append(nums)
     
    return result        

test_cases = [ "1: Geeks for geeks, 2: geeksfor geeks, 3: forGeeksgeeks 56" ,
              "geeksforgeeks" , "geeks4geeks4","S214"]

for test in test_cases:
    nums = extract_integer(s=test)
    print(nums)