N = int(input())
g = set([])
for i in range(N):
    s, t = input().split()
    g.add((s,t))
if len(g) == N:
    print("No")
else:
    print("Yes")

