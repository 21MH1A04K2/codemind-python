a=int(input())
arr=list(map(int,input().split()))
d={}
c=[]
for i in arr:
    if i not in d:
        d[i]=1
    else:
        d[i]+=1
for i,j in d.items():
    if j==1:
        c.append(i)
if len(c)==0:
    print(-1)
else:
    print(*c)