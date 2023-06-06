def prime(n):
    if n<2:
        return False
    for i in range(2,n):
        if n%i==0:
            return False
    return True
a=int(input())
c=0
for i in range(1,a+1):
    if a%i==0:
        if not prime(i):
            c+=1
print(c)