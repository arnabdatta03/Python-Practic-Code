
'''import numpy as np
l= [ ]
n=int(input("Enter:"))
for i in range(n):
    y=int(input("Enter values:"))
    l.append(y)
y=np.array(l)
print(y)
print(y.ndim)   # this .ndim function is use to see how many dimentition array is create
'''

import numpy as np
l= [[1,2,3,4],[11,22,33,41]]
a = np.array(l)
print(a)
print(a.ndim) 
