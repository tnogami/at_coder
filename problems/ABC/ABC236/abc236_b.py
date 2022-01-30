import collections
N = int(input())
A = list(map(int,input().split()))
ct = collections.Counter(A)

for i, n in ct.items():
    if n%4 != 0:
        print(i)
        break