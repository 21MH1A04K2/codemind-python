for i in range(int(input())):
    a=int(input())
    b=str(a)
    if b==b[::-1]:
        print("True")
    else:
        print("False")