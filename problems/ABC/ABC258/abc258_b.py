N = int(input())
A = [input() for _ in range(N)]

dx = (-1,-1,-1,0,0,1,1,1)
dy = (-1,0,1,-1,1,-1,0,1)

ans = 0

for i in range(N):
    for j in range(N):
        for k in range(8):
            tmp = []
            _i = i
            _j = j
            for n in range(N):
                _i += dx[k]
                _j += dy[k]
                tmp.append(A[_i%N][_j%N])
            
            ans = max(ans,int("".join(tmp)))
print(ans)