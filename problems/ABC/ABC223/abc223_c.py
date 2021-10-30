N = int(input())
lopes = []
for i in range(N):
    ab = tuple(map(float, input().split()))
    lopes.append(ab)

t = 0

for i in range(N):
    t += lopes[i][0]/lopes[i][1]

t = t/2.0

ans = 0
tmp = 0

for i in range(N):
    tmp += lopes[i][0]/lopes[i][1]
    if tmp < t:
        ans += lopes[i][0]
    else:
        tmp -= lopes[i][0]/lopes[i][1]
        t = t - tmp
        ans += t * lopes[i][1]
        break

print(ans)