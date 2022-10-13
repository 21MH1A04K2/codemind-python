n=int(input())
a=0
b=1
for i in range(2,n):
    c=a+b
    if c==n:
        print("True")
        break
    a=b
    b=c
#else:
    #print("False")
if c>n:
    print("False")