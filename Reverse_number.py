num=int(input("Enter The Number:"))
rev=0
while(num>0):
    mod=num%10
    rev=rev*10+mod
    num=num//10
print("The Reverse Number Is :",rev)