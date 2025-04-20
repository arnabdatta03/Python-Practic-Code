number=50
guess=1
print("You gess the number only 5 times")
print()
while(guess<=5):
    n= int(input("Enter Your Gessing Number : "))
    if(n>number):
        print("You gess gratter number please enter less number....")
    elif(guess==49):
        print("You are short distance from the guess ")
    elif(n<number):
        print("You gess less number enter gratter number")
    else:
        print("Yeah You Won The Game")
        print(f"you finish the game {guess} gusess")
        break
    print(f"You have left {5-guess}")
    guess=guess+1
if(guess>5):
    print("Game Over")
    
    