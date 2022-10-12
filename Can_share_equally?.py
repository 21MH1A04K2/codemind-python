a,b=map(int,input().split())
if a%2==0 and (b<a or b%2==0):
    print("YES")
else:
    print("NO")