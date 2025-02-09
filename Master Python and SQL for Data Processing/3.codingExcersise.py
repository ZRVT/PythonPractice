def find_missing_number(nums):
    nums.sort()
    number = 0
    for i in nums:
        if i == number:
            number += 1        
    return number        

find_missing_number([])

def find_common_elements(list1, list2):
    listMatching = []
    for i in list1:
        
        
        print(i)

    print(listMatching)
    return listMatching

list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]