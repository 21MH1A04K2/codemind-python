n=int(input())
arr=list(map(int,input().split()))
a,b=map(int,input().split())
c=0
for i in arr:
    if i<a or i>b:
        print(i,end=' ')
        c=1
if c==0:
    print("-1")