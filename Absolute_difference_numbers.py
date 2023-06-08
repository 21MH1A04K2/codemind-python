a,b=map(int,input().split())
c=str(a)
d=c[:b]
e=c[-b:]
x=int(d)
y=int(e)
print(abs(x-y))