a=int(input())
l=list(map(int,input().split()))
c=a//2
s=0
p=0
for i in range(c):
    s+=l[i]
for j in range(c,n):
    p+=l[j]
d=abs(s-p)
if d%4==0:
    print('X')
else:
    print('Y')
    
