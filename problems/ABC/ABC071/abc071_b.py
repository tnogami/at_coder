import string

aset = set([])
for i in input():
    aset.add(i)

for i in string.ascii_lowercase:
    if not i in aset:
        print(i)
        break
else:
    print("None")