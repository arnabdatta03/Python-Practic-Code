n = [2,3,4,56,7]
multi = int(input("Which number you want to multiply to this list:"))
for i in range(len(n)):
    n[i] = n[i] * multi
print(n)