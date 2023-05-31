a=int(input())
b=list(map(int,input().split()))
l=[]
for i in range(0,a,2):
    x=b[i] # 1 3 5 7 
    y=b[i+1] # 2 2 2 2 
    for i in range(y): # 0 1
        l.append(x)
print(*l)