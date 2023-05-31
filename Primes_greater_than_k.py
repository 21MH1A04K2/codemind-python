def prime(n):
    if n<2:
        return False
    for i in range(2,n):
        if n%i==0:
            return False
    return True
x=int(input())
c=0
y=map(int,input().split())
z=int(input())
for i in y:
    if prime(i):
        if i>=z:
            c+=1
print(c)