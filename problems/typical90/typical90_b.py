def dfs(s):
    global N
    global ans

    if len(s) == N:
        ans.append(s)
        return

    op = s.count("(")
    cl = s.count(")")

    if op == N//2:
        next_dfs = [")"]    
    elif op == cl:
        next_dfs = ["("]
    else:
        next_dfs = ["(", ")"]

    for k in next_dfs:
        dfs(s+k)

N = int(input())

ans = []

if N % 2 == 1 :
    print("")
else:
    dfs("")
    ans.sort()
    for a in ans:
        print(a)
