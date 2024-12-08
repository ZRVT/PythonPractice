def max_num(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num3 and num2 >= num1:
        return num2
    else:
        return num3
    
print(max_num(6,10,5))

#operators 
# == equal to
# != not equal to
# > greater than
# < less than
# >= greater than or equal to
# <= less than or equal to