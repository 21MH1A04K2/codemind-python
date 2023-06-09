a=int(input())
b=list(map(int,input().split()))
d={}
c=[]
for i in b:
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
    print(max(*c))
    