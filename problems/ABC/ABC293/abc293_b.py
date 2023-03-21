N = int(input())
A = list(map(int,input().split()))
is_called = [False]*N

for i, a in enumerate(A):
    if not is_called[i]:
        is_called[a-1] = True

ans = []

for i, c in enumerate(is_called, 1):
    if not c:
        ans.append(i)

print(len(ans))
print(*ans)
