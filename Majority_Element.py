a=int(input())
b=list(map(int,input().split()))
co=0
for i in b:
    c=b.count(i)
    if c>a//2:
        co=i
print(co)
   
