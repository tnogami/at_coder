N = int(input())
ans = 100000

for _ in range(N):
    l, r = map(int, input().split())
    ans -= r - l + 1

print(100000-ans)