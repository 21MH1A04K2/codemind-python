def prime(n):
    if n<2:
        return False
    for i in range(2,n):
        if n%i==0:
            return False
    return True
x=int(input())
y=map(int,input().split())
l=[]
for i in y:
    if prime(i):
        l.append(i)
p=sum(l)/len(l)
print("%.2f" %p)  