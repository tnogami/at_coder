N, M = map(int, input().split())
S = list(map(int,input().split()))
T = list(map(int,input().split()))

first = True
ans = 0
if set(T) <= set(S):
    for t in T:
        if first:
            if t == S[0]:
                ans += 1
            else:
                tmp = N
                for i in range(N):
                    if S[i+1] == t:
                        tmp = i+1
                        break
                for i in range(N):
                    if S[-(i+1)] == t:
                        tmp = min(tmp, i+1)
                ans += tmp + 1
                first = False
                pre_t = t
        else:
            if pre_t == t:
                ans += 1
            else:
                ans += 2
                pre_t = t
    print(ans)
else:
    print(-1)




