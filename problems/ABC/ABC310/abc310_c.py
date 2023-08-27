N = int(input())

g = set()
ans = 0
for _ in range(N):
    s = input()
    if s in g:
        continue

    g.add(s)
    g.add(s[::-1])
    ans += 1

print(ans)
