n=int(input())
arr=list(map(int,input().split()))
o=0
for i in arr:
    if i%2!=0:
        o=o+i
print(o)
