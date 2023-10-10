N, M = map(int, input().split())
A = list(map(int, input().split()))

scores = [i for i in range(1, N + 1)]

for i in range(N):
    S = input()
    for j in range(M):
        if S[j] == "o":
            scores[i] += A[j]

m = max(scores)
mult_flag = False if scores.count(m) == 1 else True

for i, score in enumerate(scores):
    if score == m:
        if mult_flag:
            print(1)
        else:
            print(0)
    else:
        not_solved = []
        for j in range(M):
            if S[j] == "x":
                not_solved.append(A[j])
        not_solved.sort(reverse=True)
        ct = 0
        for ns in not_solved:
            ct += 1
            score += ns
            if score >= m:
                break
        print(ct)
