a=int(input())
b=a*a
b=str(b)
if int(b[-len(str(a)):])==a:
    print("Automorphic Number")
else:
    print("Not an Automorphic Number")