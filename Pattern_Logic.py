import time as t
initial=t.time()
n=int(input("Enter the Rows:"))
bo=int(input("Enter the Boolean 0 or 1:"))
new=bool(bo)
if(new==True):
    print("You Entered True")
    for i in range(1,n+1):
        pattern= "*"*i
        print(pattern)

elif(new==False):
    print("You Entered False")
    for i in range(n,0,-1):
        pattern="*"*i
        print(pattern)
j=t.time()-initial
print(j)
'''
# In this code If You Bollean 1 that means its True That Print Normal patern
 and if you type 0 that means its false that prints decressing pattern.
'''
