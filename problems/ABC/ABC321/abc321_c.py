K = int(input())


def dfs(s):
    global ans
    ans.append(int(s))
    if s[-1] == '0':
        return

    for i in range(0, int(s[-1])):
        dfs(s+str(i))


ans = []

for i in range(1, 10):
    dfs(str(i))

ans.sort()

print(ans[K-1])
