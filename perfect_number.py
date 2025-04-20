
number = int(input("Enter the number: "))
sum= 0
for divisor in range(1, number):
    if number % divisor == 0:
        sum=sum+divisor
if sum == number:
    print(" This is a perfect number",number)
else:
    print("This is not a perfect number",number)
