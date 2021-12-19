import collections
N = int(input())
ct = collections.Counter()

for _ in range(N):
    name = input()
    ct[name] += 1

l = [(name, v) for name, v in ct.items()]
l.sort(key=lambda x: x[1])
print(l[-1][0])