num=int(input("Enter the Number:"))
d=0
for i in range (1,num+1):
    fact=1
    for j in range (1,i+1):
        fact=fact*j
    d=d+fact
print(d)