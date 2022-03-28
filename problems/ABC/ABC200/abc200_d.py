N = int(input())
A = list(map(int,input().split()))
A = list(map(lambda x: x%200, A))

dp = [[]*200 for _ in range(N+1)]
