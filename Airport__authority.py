c=[]
co=0
for i in range(int(input())):
    a=int(input())
    c.append(a)
t=int(input())
for i in c:
    if i>t:
        co+=2
    else:
        co+=1
print(co)