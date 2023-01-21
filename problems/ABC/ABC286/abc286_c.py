N, A, B = map(int, input().split())
S = input()

ans = 10**21
for i in range(N):
    start = i
    end = (N-1+i)%N
    diff_ct = 0
    for j in range(N//2):
        if S[(start+j)%N] != S[(end-j)%N]:
            diff_ct += 1
    ans = min(ans, diff_ct*B+i*A)
print(ans)
