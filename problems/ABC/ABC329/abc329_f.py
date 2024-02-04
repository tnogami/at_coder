N, Q = map(int, input().split())
C = list(map(int, input().split()))
balls = [set([c]) for c in C]
for _ in range(Q):
    query = list(map(int, input().split()))
    a, b = query[0], query[1]
    a -= 1
    b -= 1
    balls[b] = balls[b].union(balls[a])
    balls[a] = set()
    print(len(balls[b]))
