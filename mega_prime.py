def prime(n):
    if n<2:
        return False
    for i in range(2,n):
        if n%i==0:
            return False
    return True
a=int(input())
c=0
if prime(a):
    a=str(a)
    for  i in a:
        i=int(i)
        if prime(i):
            c+=1
    if c==len(str(a)):
        print("Mega Prime")
    else:
        print("Not Mega Prime")
else:
    print("Not Mega Prime")

    
        