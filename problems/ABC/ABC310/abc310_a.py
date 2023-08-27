N, P, Q = map(int, input().split())
D = list(map(int, input().split()))

ans = P

print(min(ans, Q+min(D)))
