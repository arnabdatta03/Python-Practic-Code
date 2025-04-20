range1=int(input("Enter the first range:"))
range2=int(input("Enter the second range:"))
temp=range1
while temp<=range2:
    if temp%2!=0:
        print(temp)
    temp=temp+1