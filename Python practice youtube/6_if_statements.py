is_male = False
is_tall = False
is_age = "30"

if is_male:
    print("You are a male")
    # Anything after the If statement will be considered true
else: 
    print("You are not a Male")
    #and the else is the false statement. You don't need to define this. 

if is_male or is_tall:
    #Or & And Operators can be used to define the if statements
    print("You are a male or tall or both")
else:
    print("You are neither")

if is_male and is_tall:
    print("You are a tall male and age " + is_age)
elif is_male and not(is_tall):
    print("You are a male but not tall and age " + is_age) 
    #use the elif to determine another if statement
    #use and not() to determine what to do when it is false
elif not(is_male) and not(is_tall):
    #you can use not for multiple determinations
    print("You are a female but not tall and age " + is_age)
else:
    print("You are a tall female and age " + is_age)