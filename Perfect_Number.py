 n=int(input())#10
sum=0
for i in range(1,n):# 1,10
    if(n%i==0):
        sum=sum+i
if(sum==n):
    print("True")
else:
    print("False")
    
    
    