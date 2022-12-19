n=int(input())
arr=list(map(int,input().split()))
a=sum(arr)//n
if a in arr:
    print("True")
else:
    print("False")