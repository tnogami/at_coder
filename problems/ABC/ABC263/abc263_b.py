N = int(input())
P = list(map(int,input().split()))
cur = P[-1]
ct = 1

while cur != 1:
    cur = P[cur-2]
    ct += 1

print(ct)