r,c=map(int,input().split())
mat=[]
s=0
for i in range(r):
    x=list(map(int,input().split()))
    mat.append(x)
    s+=sum(x)
print(s)