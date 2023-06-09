a=int(input())
b=int(input())
c=[]
e=[]
co=0
for i in range(a,b+1):
    c.append(i)
for i in range(len(c)):
    for j in range(i,len(c)):
        d=c[i:j+1]
        e.append(d)
for i in e:
    p=sum(i)
    if p%2!=0:
        co+=1
print(co)