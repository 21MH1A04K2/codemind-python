def prime(n):
    if n<2:
        return False
    for i in range(2,n):
        if n%i==0:
            return False
    return True
for i in range(int(input())):
    a=int(input())
    f=a+1
    b=a-1
    while True:
        if prime(f) and prime(b):
            print(min(f,b))
            break
        if prime(a):
            print(a)
            break
        if prime(f):
            print(f)
            break
        if prime(b):
            print(b)
            break
        
        f+=1
        b-=1
    