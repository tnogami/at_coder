Q = int(input())
ans = []

for _ in range(Q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        ans.append(query[1])
    elif query[0] == 2:
        print(ans[-query[1]])

        