s = [i for i in input()]
s = set(s)

if len(s) == 1:
    print(1)
elif len(s) == 2:
    print(3)
else:
    print(6)