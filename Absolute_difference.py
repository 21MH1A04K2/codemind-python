def prime(n):
    if n<2:
        return False
    for i in range(2,n):
        if n%i==0:
            return False
    return True
a=int(input())
b=list(map(int,input().split()))
c=[]
d=[]
for  i in b:
    if prime(i):
        c.append(i)
    else:
        d.append(i)
p=1
q=1
for i in c:
    p*=i
for j in d:
    q*=j
print(abs(p-q))