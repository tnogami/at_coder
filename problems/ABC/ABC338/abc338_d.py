from itertools import accumulate

N, M = map(int, input().split())
X = list(map(int,input().split()))
X = list(map(lambda x: x-1, X))

acc_forwards = [0]*(N+1)

cost = 0
for k in range(len(X)-1):
    start = X[k]
    end = X[k+1]
    if abs(end - start) <= N // 2:
        cost += abs(end - start)
        length = abs(end - start)
        additional_cost = N - length - length
        if start > end:
            start, end = end, start
        acc_forwards[start] += additional_cost
        acc_forwards[end] -= additional_cost
    else:
        cost += N - abs(end - start)
        length = N - abs(end - start)
        additional_cost = N - length - length
        acc_forwards[0] += additional_cost
        if start > end:
            start, end = end, start
        acc_forwards[start] -= additional_cost
        acc_forwards[end] += additional_cost

acc_forwards = list(accumulate(acc_forwards))
ans = cost + min(acc_forwards)
print(ans)
