from itertools import permutations

N, M = map(int, input().split())
S = [list(input()) for _ in range(N)]

for ss in permutations(S, N):

    ret = True
    for i in range(N-1):
        ct = 0
        for m in range(M):
            if ss[i][m] != ss[i+1][m]:
                ct += 1
        
        if 1 < ct:
            ret = False 

    if ret:
        print("Yes")
        break
else:
    print("No")




