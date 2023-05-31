def prime(n):
    if n<2:
        return False
    for i in range(2,n):
        if n%i==0:
            return False
    return True
a=int(input())
c=0
x=map(int,input().split())
for i in x:
    if prime(i):
        c+=1
print(c)