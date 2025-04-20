lst=[]
odd=[]
even=[]
esum=0
osum=0
no=int(input("Enter How Many Items:"))
for i in range(0,no):
    k=int(input("Enter the item:"))
    lst.append(k)
print("The List is:",lst)

#print(len(lst))
for i in range(0,len(lst)):
    if lst[i]%2==0:
        even.append(lst[i])
        esum=esum+lst[i]
    else:
        odd.append(lst[i])
        osum=osum+lst[i]

print("The Even List is:",even)
print("The Odd List is:",odd)
print("The Even No List sum is:",esum)
print("The Odd No List sum is:",osum)
