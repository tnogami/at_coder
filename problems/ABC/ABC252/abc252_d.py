from collections import Counter
N = int(input())
A = list(map(int,input().split()))
ct = Counter(A)
# A.sort()
# d = dict()

# i = 0
# for a in A:
#     if a not in d:
#         d[a] = i
#     i += 1

# ans = 0
# for a in A:
#     ans += d[a]*(N-d[a]-ct[a])

# print(ans)

ans = N*(N-1)*(N-2)//6
for k in ct.values():
    if 3 <= k:
        ans -= k*(k-1)*(k-2)//6
    if 2 <= k:
        ans -= k*(k-1)//2 * (N-k)

print(ans)