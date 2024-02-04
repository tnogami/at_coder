
from itertools import accumulate

N, K = map(int, input().split())
A = list(map(int, input().split()))

score = 0
if len(A) % 2 == 0:
    for i in range(len(A)//2):
        score += A[2*i+1] - A[2*i]
else:
    score = 10**21
    init_score = 0
    for i in range(len(A)//2):
        init_score += A[2*i+2] - A[2*i+1]

    score = init_score
    tmp = init_score
    for i in range(1, len(A)):
        if i % 2 == 0:
            tmp -= A[i] - A[i-2]
            tmp += A[i-1] - A[i-2]
            score = min(score, tmp)
        else:
            tmp -= A[i+1] - A[i]
            tmp += A[i+1] - A[i-1]
            score = min(score, tmp)

print(score)

