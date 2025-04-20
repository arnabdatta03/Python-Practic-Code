n = int(input("Enter the number :"))
sum = 0
order = len(str(n))
temp = n
while(n>0):
    digit = n%10
    sum = sum+digit **order
    n = n//10
if(sum == temp):
    print("It is an amstrong number !!!")
else :
    print("It is not an amstrong number !!!")
 
