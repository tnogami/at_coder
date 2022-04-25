S = input()
big = False
small = False
a = True
t = set()
for s in S:
    if s.islower():
        small = True
    if s.isupper():
        big = True
    if s in t:
        a = False
    t.add(s)

if big and small and a:
    print("Yes")
else:
    print("No")    
