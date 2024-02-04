N = int(input())
A = list(map(int,input().split()))

d = {mae:idx+1 for idx,mae in enumerate(A)}

# -2 のインデックスを取得
ans = [d[-1]]

while len(ans) < N:
    ans.append(d[ans[-1]])

print(*ans)
