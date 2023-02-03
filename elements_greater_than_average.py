n=int(input())
e=list(map(int,input().split()))
s=sum(e)
d=s//n
c=0
for i in range(n):
    if(e[i]>=d):
        c+=1
print(c)

