number=18
number_of_guess=1
print("                 This Is A Number Of Guesses Game !!! Here You Can Take Only 9 Attempts To Guess The Number")
print("              ------------------------------------------------------------------------------------------------")
while(number_of_guess<=9):
    guess=int(input("Enter Your Guess:"))
    if(guess<18):
        print("You Guess To Low Increase Your Guess")
    elif(guess>18):
        print("You Guess To High Increase Your Guess")
    else:
        print("Congrulation You The Game !!!")
        print("You Finish {number_of_guess} Number Of Gusess")
        break
    #number_of_guess+=1
    print("Your Left Number Of Guess Is:",9-number_of_guess)
    number_of_guess+=1
if(number_of_guess>9):
    print("The Game Is Over !!!")