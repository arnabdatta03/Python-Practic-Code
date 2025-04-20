import time
marked=time.time()

print(marked)
i=0
while(i<5):
    print("Arnab")
    i=i+1
print("While Loop time is:",time.time()-marked)
marked1=time.time()
for i in range(5):
    print("Datta")
print("For Loop time is:",time.time()-marked1)