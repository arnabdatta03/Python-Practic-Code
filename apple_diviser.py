apple=int(input("How many apple enter first:"))
min=int(input("Enter the minimum range:"))
max=int(input("Enter the maximum range:"))
for i in range(max,min+1):
    print("aaa")
    if(apple%i==0):
        print(f"{i} is divisable of {apple}")
    else:
       print(f"{i} is not divisable of {apple}")