def prime(n):
    if n<2:
        return False
    for i in range(2,n):
        if n%i==0:
            return False
    return True
a=int(input())
c=[]
d=0
for i in range(1,a+1):
    if a%i==0:
        c.append(i)
for i in c:
    if not prime(i):
        d+=1
print(d)