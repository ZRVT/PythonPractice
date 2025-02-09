secret_work:str = "giraffe"
guess:str = ""
guess_count:int = 0
guess_limit:int = 3
out_of_guesses:bool = False


while guess != secret_work and not(out_of_guesses):
    if guess_count < guess_limit:
        guess = input("Enter guess: ")
        guess_count += 1
        # i added the below if statement to make code clearer in terms of output. 
        if guess_count == 1:
            print("You have 2 guesses left")
        elif guess_count == 2:
            print("You have 1 guess left")
    else: 
        out_of_guesses = True

if out_of_guesses:
    print("Out of guesses, You lose!")
else:
    print("You win!")