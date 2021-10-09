N, M = map(int, input().split())
A = [input() for i in range(2*N)]

rank = [[i, 0] for i in range(2*N)]

for m in range(M):

    for i in range(N):
        a = rank[2*i][0]
        b = rank[2*i+1][0]

        if A[a][m] == A[b][m]:continue
        if (A[a][m] == "G" and A[b][m] == "C") or (A[a][m] == "C" and A[b][m] == "P") or (A[a][m] == "P" and A[b][m] == "G"):
            rank[2*i][1] = rank[2*i][1] + 1
            continue
#        if (A[a][m] == "G" and A[b][m] == "C") or (A[a][m] == "C" and A[b][m] == "P") or (A[a][m] == "P" and A[b][m] == "G"):
        rank[2*i+1][1] = rank[2*i+1][1] + 1

    rank.sort(key=lambda x: x[0])
    rank.sort(key=lambda x: x[1], reverse=True)


for r in rank:
    print(r[0]+1)



