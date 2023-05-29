m = input()
c = []
s = 'aeiou'
for i in m:
    if i.isalpha():
        c.append(i)
d = set(c)
e = 0
for i in s:
    if i in d:
        e+=1
if e == 5:
    print("True")
else:
    print("False")