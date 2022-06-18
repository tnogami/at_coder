from bisect import bisect

A, B, Q = map(int, input().split())
S = [int(input()) for _ in range(A)]
T = [int(input()) for _ in range(B)]
S = [-10**12] + S
S.append(10**12)
S.append(10**13)
T = [-10**12] + T
T.append(10**12)
T.append(10**13)

for _ in range(Q):
    q = int(input())

    ans = 10 ** 12

    #神社から訪問
    idx = bisect(S,q)

    tmp = 0
    #右から訪問
    tmp += S[idx] - q
    #左右の近い方の寺に訪問
    idx2 = bisect(T, S[idx])
    tmp += min(S[idx]-T[idx2-1], T[idx2]-S[idx])

    ans = min(ans, tmp)

    tmp = 0
    #左から訪問
    tmp += q - S[idx-1]
    #左右の近い方の寺に訪問
    idx2 = bisect(T, S[idx-1])
    tmp += min(S[idx-1]-T[idx2-1], T[idx2]-S[idx-1])

    ans = min(ans, tmp)
    

    #寺から訪問
    idx = bisect(T,q)
    
    tmp = 0
    #右から訪問
    tmp += T[idx] - q
    #左右の近い方の寺に訪問
    idx2 = bisect(S, T[idx])
    tmp += min(T[idx]-S[idx2-1], S[idx2]-T[idx])

    ans = min(ans, tmp)

    tmp = 0
    #左から訪問
    tmp += q - T[idx-1]
    #左右の近い方の寺に訪問
    idx2 = bisect(S, T[idx-1])
    tmp += min(T[idx-1]-S[idx2-1], S[idx2]-T[idx-1])

    ans = min(ans, tmp)
    
    print(ans)


