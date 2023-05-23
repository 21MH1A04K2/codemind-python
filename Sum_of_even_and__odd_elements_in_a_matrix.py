r,c=map(int,input().split())
mat=[]
es=0
os=0
for i in range(r):
    x=list(map(int,input().split()))
    mat.append(x)
for i in range(r):
    for j in range(c):
        if mat[i][j]%2==0:
            es+=mat[i][j]
        else:
            os+=mat[i][j]
print(es,os)