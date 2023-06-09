a,b=map(int,input().split())
c=list(map(int,input().split()))
d=[]
e=[]
for i in range(len(c)):
    for j in range(i,len(c)):
        d=c[i:j+1]
        e.append(d)
c=0
for i in e:
    p=sum(i)
    if p==b:
        c+=1
print(c)

    