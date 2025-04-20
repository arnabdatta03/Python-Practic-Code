num = int(input("Enter a number: "))
num1 = num
sum= 0
while num > 0:
    fact = 1
    for i in range(1, num % 10+1):
     fact = fact* i
    sum= sum+ fact
    num = num // 10
if sum == num1:
    print("It is a strong number")
else:
    print("It is not a strong number")
