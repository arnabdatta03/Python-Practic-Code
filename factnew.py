n=int(input("Enter the number:"))
fact=1
for i in range (1,n+1):
    fact=fact*i
    if n>i:
        print(i,"X",end=" ")
    else:
        print(i,"=",end=" ")

print(fact)