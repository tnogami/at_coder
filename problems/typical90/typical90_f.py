
def cal_nex(S):
    ret = [[N]*26 for i in range(N+1)]

    for i in range(N-1, -1, -1):
        for j in range(26):
            ret[i][j] = ret[i+1][j]
        
        idx = ord(S[i]) - ord("a")
        ret[i][idx] = i

    return ret

N, K = map(int, input().split())
S = input()

nex = cal_nex(S)







