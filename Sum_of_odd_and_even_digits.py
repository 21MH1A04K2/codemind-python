n=int(input())
arr=list(map(int,input().split()))
s1=0
s2=0
for i in range(1,len(arr),2):
    s1=s1+arr[i]
for i in range(0,len(arr),2):
    s2=s2+arr[i]
c=abs(s1-s2)
if c==0:
    print("YES")
else:
    print("NO")
        
        