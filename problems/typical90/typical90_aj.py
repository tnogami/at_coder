N, Q = map(int, input().split())
points = []
points_tr = []
for _ in range(N):
   x, y = map(int, input().split())
   points.append((x,y))
   points_tr.append((x+y, x-y))

min_a = min(points_tr, key=lambda x : x[0])[0]
min_b = min(points_tr, key=lambda x : x[1])[1]
max_a = max(points_tr, key=lambda x : x[0])[0]
max_b = max(points_tr, key=lambda x : x[1])[1]

for _ in range(Q):
    q = int(input())
    q -= 1
    ans = max(points_tr[q][0]-min_a, points_tr[q][1]-min_b, max_b-points_tr[q][1], max_a-points_tr[q][0])
    print(ans)
