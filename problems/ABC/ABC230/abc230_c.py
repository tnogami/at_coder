N, A, B = map(int, input().split())
P, Q, R, S = map(int, input().split())

def check(x, y):
    return y+1 - A == x+1 - B or y+1 - A == -(x+1 - B)

ans = [[] for i in range(Q-P+1)]

for i in range(P,Q+1):
    for j in range(R,S+1):
        if check(j-1, i-1):
            ans[i-P].append("#")
        else:
            ans[i-P].append(".")

for a in ans:
    print("".join(a))
