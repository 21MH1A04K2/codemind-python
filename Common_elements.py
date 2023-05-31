m,n = map(int,input().split())
x = list(map(int,input().split()))
y = list(map(int,input().split()))
c = []
for i in x:
    if i in y:
        c.append(i)
for j in y:
    if j in x:
        c.append(j)
l = []
for n,i in enumerate(c):
    if i not in c[:n]:
        l.append(i)
print(*l)