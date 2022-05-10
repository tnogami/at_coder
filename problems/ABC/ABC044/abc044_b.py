from collections import Counter
w = input()
ct = Counter(w)

if all([i%2==0 for i in ct.values()]):
    print("Yes")
else:
    print("No")


