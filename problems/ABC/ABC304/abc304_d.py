from bisect import bisect
W, H = map(int, input().split())
N = int(input())
ichigos = [tuple(map(int, input().split())) for _ in range(N)]
A = int(input())
A_list = list(map(int,input().split()))
B = int(input())
B_list = list(map(int,input().split()))

ct = dict()

for ichigo in ichigos:
    w_index = bisect(A_list, ichigo[0])
    h_index = bisect(B_list, ichigo[1])

    if (w_index, h_index) in ct:
        ct[(w_index, h_index)] += 1
    else:
        ct[(w_index, h_index)] = 1

ans = list(ct.values())
M = max(ans)

if len(ct) == (A+1) * (B+1):
    m = min(ans)
else:
    m = 0
print(m, M)
