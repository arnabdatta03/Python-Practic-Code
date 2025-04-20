a={}
no=int(input("Enter How Many Keys With Value:"))
for i in range(0,no):
    key=input("Enter the Key:")
    value=input("Enter the Value:")
    a.update({key:value})

print("The Dictionary is:",a)