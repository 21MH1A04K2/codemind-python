s=int(input())
sum=0
product=1
n1 = s

while(s>0):
    d=s%10
    sum=sum+d
    product=product*d
    s=s//10

if(sum==product):
    print("Spy Number".format(n1))
else:
    print("Not Spy Number")
