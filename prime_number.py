def prime(n):
    if n<2:
        return False
    for i in range(2,n):
        if n%i==0:
            return False
    return True
a=int(input())
if prime(a):
    print("prime")
else:
    print("not a prime")