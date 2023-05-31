a=int(input())
l=[]
b=list(map(int,input().split()))
for i in range(0,a,2):
    x=b[i]
    y=b[i+1]
    for i in range(y):
        l.append(x)
print(*l)