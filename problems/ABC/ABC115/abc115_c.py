N, K = map(int, input().split())
heights = [int(input()) for _ in range(N)]
heights.sort()

ans = 10**12
for i in range(N-K+1):
    h_min = heights[i]
    h_max = heights[i+K-1]
    ans = min(ans, h_max-h_min)
print(ans)
