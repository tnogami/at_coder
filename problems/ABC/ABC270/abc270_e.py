

N, K = map(int, input().split())
A = list(map(int,input().split()))
B = A[:]
B.sort()
idx = 0
still_there = N
eat = 0

while K:
    if B[idx]-eat == 0:
        still_there -= 1
        idx+=1
        continue
    if (B[idx]-eat)*still_there <= K:
        K -= (B[idx]-eat)*still_there
        eat += (B[idx]-eat)
        still_there -= 1
        idx += 1
    else:
        loop = K // still_there
        eat += loop
        K -= loop*still_there
        k = 0
        for i in range(N):
            if k == K:break
            if eat < A[i]:
                A[i] -= 1
                k += 1
        break

ans = []

for a in A:
    if a < eat:
        ans.append(0)
    else:
        ans.append(a-eat)

print(*ans)