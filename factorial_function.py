
def fact_iiterative(n):
    fact=1
    for i in range(n):
        fact=fact*(i+1)
    return fact



def fact_recursive(n):
        
        if n==1:
            return 1
        else:
            return n*(fact_recursive(n-1))
        
        

number=int(input("Enter the number:"))
print("In Iterative Function The output is:",fact_iiterative(number))
print("In Recursive Function The output is:",fact_recursive(number))

