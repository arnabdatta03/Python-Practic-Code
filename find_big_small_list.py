lst=[]# Defining a Empty List
n=int(input("Enter How Many List Items You Want to Store:"))
for i in range(0,n):
    ele=int(input("Enter the item one by one:"))
    lst.append(ele)

print("The List is:",lst)

big=lst[0]
small=lst[0]
for i in range(0,len(lst)):
    if lst[i]>=big:
        big=lst[i]

print("The Biggest Element is:",big)

for i in range(0,len(lst)):
    if lst[i]<=small:
        small=lst[i]

print("The Smallest Element is:",small)