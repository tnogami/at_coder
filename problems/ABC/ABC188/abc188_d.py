N, C = map(int, input().split())
event = []

for i in range(N):
    a, b, c = map(int, input().split())
    event.append((a,c))
    event.append((b+1, -c))

event.sort()
day = 0
price = 0
ans = 0

for e in event:

    if price < C:
        ans += price*(e[0]-day)
    else:
        ans += C*(e[0]-day)

    price += e[1]
    day = e[0]

print(ans)
