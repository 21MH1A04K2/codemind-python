def prime(n):
    if n<2:
        return False
    for i in range(2,n):
        if n%i==0:
            return False
    return True
a=int(input())
if prime(a):
    a=str(a)
    a=a[::-1]
    if prime(int(a)):
        print("circular prime")
    else:
        print("prime but not a circular prime")
else:
    print("not prime")
        