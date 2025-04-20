#while True:
    
candy=9
user1=int(input("How many candyes you want:"))
if user1<=candy:
    for i in range(0,user1):
        print("Given Candy=",i+1)
    print("Thank you please visit again")
else:
    for k in range(0,candy):
        print("Given candy=",k+1)
    print("Sorry no more candy available !!!")

 