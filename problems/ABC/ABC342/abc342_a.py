from collections import Counter
S = list(input())

ct = Counter(S)

for k, v in ct.items():
    if v == 1:
        break

for i, s in enumerate(S, 1):
    if s == k:
        print(i)
        break
