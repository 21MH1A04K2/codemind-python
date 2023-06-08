a=int(input())
b=len(str(a))
t=a
su=0
while a:
    c=a%10
    su=su+(c**b)
    a=a//10
    b-=1
if t==su:
    print("True")
else:
    print("False")
    