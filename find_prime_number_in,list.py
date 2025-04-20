lst=[]# Defining a Empty List
n=int(input("Enter How Many List Items You Want to Store:"))
for i in range(0,n):
    ele=int(input("Enter the item one by one:"))
    lst.append(ele)

print("The List is:",lst)

print("The Prime Numbers Are:")
for i in range(0,len(lst)):
    c=0
    for j in range(1,(lst[i]+1)):
        if lst[i]%j==0:
            c=c+1
    if c==2:
        print(lst[i],end=" ")