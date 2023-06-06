a=int(input())
b=a*a
su=0
while b:
    d=b%10
    su+=d
    b=b//10
if su==a:
    print("Neon Number")
else:
    print("Not Neon Number")