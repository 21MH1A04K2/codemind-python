n=int(input())
s=list(map(int,input().split()))
a=sum(s)
d=a//n
c=0
for i in range(n):
  if(s[i]<=d):
      c+=1
print(c)