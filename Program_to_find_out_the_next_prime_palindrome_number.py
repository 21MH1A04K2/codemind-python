def prime(n):
    if n<2:
        return False
    for i in range(2,n):
        if n%i==0:
            return False
    return True
def pnd(n):
    n=str(n)
    if n==n[::-1]:
        return True
    return False
a=int(input())
b=a+1
while True:
    if prime(b) and pnd(b):
        print(b)
        break
    b+=1
    
        
        