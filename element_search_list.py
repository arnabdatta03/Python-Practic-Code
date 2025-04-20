lst=[]# Defining a Empty List
n=int(input("Enter How Many List Items You Want to Store:"))
for i in range(0,n):
    ele=int(input("Enter the item one by one:"))
    lst.append(ele)

print("The List is:",lst)

c=0
search=int((input("Enter the Element You Want to Search:")))
for i in range(0,len(lst)):
    if lst[i]==search:
        c=c+1
    
if c>0:
    print("Yes Present")
else:
    print("Not Present")
       