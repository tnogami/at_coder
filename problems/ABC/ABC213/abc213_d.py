import sys
sys.setrecursionlimit(10**9)

def dfs(i):
    visited[i] = True
    ans.append(str(i+1))

    flag = False
    for j in nodes[i]:
        if visited[j] == True : continue
        flag = True
        dfs(j)
        ans.append(str(i+1))

N = int(input())
nodes = [[] for i in range(N)]
visited = [-1 for i in range(N)]
ans = []

for i in range(N-1):
    a,b =  map(int,input().split())
    nodes[a-1].append(b-1)
    nodes[b-1].append(a-1)

for i in range(N):
    nodes[i].sort()

dfs(0)

print(" ".join(ans))