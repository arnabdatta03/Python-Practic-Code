number =int(input("Enter the number :"))
temp = number
reverse = 0
while(number>0):
    c = number%10
    reverse = reverse*10+c
    number=number//10

if temp == reverse:
        print("The number is palindrome !!!")
else:
        print("The number is not palindrome !!!")

