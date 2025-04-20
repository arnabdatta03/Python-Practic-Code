sort=lambda a:a[1]           #This is lambda condition uses
def sort(a):
    return a[1]              #This is normal function uses



a=[[10,42],[3,4],[89,90],[1,2]]
a.sort(key=sort)
print(a)