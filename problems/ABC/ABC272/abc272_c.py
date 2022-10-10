N = int(input())
A = list(map(int,input().split()))
odd = []
even = []

for a in A:
    if a%2 == 0:
        even.append(a)
    else:
        odd.append(a)

even.sort()
odd.sort()

ans = -1

if 2 <= len(even):
    ans = max(ans, even[-1]+even[-2])

if 2 <= len(odd):
    ans = max(ans, odd[-1]+odd[-2])

print(ans)
