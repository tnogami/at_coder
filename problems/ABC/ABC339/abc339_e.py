def max_length_subsequence(A, D):
    N = len(A)
    max_length = 0
    start = 0

    for end in range(N):
        while start < end and abs(A[end] - A[start]) > D:
            start += 1
        max_length = max(max_length, end - start + 1)

    return max_length

N, D = map(int, input().split())
A = list(map(int, input().split()))

print(max_length_subsequence(A, D))