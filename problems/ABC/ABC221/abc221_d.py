N = int(input())
event = []
ans = [0]*(N+1)

for i in range(N):
    a, b = map(int, input().split())
    event.append((a, 1))
    event.append((a+b, -1))

event.sort()

day = 0
num = 0

for e in event:
    ans[num] += e[0]-day
    num += e[1]
    day = e[0]

print(" ".join(list(map(str, ans[1:]))))