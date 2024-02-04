from collections import Counter
S = input()
ct = Counter(list(S))

l = [(-num, s) for s, num in ct.items()]
l.sort(key=lambda x: x[1])
l.sort()
print(l[0][1])