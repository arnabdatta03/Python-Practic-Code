qun = int(input("Enter the quentaty :"))
price = float(input("Enter the price :"))
dis = 10
#\if qun>1000:
    #dis = 10
#else:
    #dis = 0
#toexp = qun*price-qun*price*dis/100
toe = price*qun
toex = dis/100*toe
toexp = toe-toex
print("Total expencess is RS=",toexp)
