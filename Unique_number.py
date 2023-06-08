a=input()
d={}
for i in a:
    i=int(i)
    if i not in d:
        d[i]=1
    else:
        d[i]+=1
b1,b2=0,0
for i,j in d.items():
    b1+=1
    if j==1:
        b2+=1
if b1==b2:
    print("Unique Number")
else:
    print("Not Unique Number")
    
