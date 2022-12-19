n=int(input())
arr=list(map(int,input().split()))
e=0
for i in range(0,len(arr),2):
        e=e+arr[i]
print(e)
