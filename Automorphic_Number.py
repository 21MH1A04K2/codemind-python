n=int(input())
a=n*n
b=10**len(str(n))
if a%b==n:
    print('Automorphic Number')
else:
    print('Not an Automorphic Number')