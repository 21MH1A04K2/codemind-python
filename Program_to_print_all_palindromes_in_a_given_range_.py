def palindrome(n):
    n=str(n)
    if n==n[::-1]:
        return True
    else:
        return False
a=int(input())
b=int(input())
for i in range(a,b):
    if palindrome(i):
        print(i,end =' ')