N = int(input())
P = list(map(int,input().split()))

bgst = 10**6
count = 0
for p in P:
    if p < bgst:
        count += 1
        bgst = p

print(count)