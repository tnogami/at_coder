from itertools import permutations
N, H, W = map(int, input().split())
AB = [tuple(map(int, input().split())) for _ in range(N)]


for order in permutations(AB, N):
    field = [[0] * W for _ in range(H)]
    dfs(0, field)