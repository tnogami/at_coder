N, P = map(int, input().split())
A = list(map(int,input().split()))

ct = 0

for a in A:
    if a < P : ct += 1
print(ct)
