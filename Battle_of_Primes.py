def prime(n):
    if n<2:
        return False
    for i in range(2,n):
        if n%i==0:
            return False
    return True
a=int(input())
b=int(input())
c=a+b
c1=0
while 1:
    c=c+1
    c1+=1
    if prime(c):
        break 
print(c1)