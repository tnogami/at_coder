import sys
sys.setrecursionlimit(10**7)

const = 10**2
ladder = [[] for _ in range(const)]
n = int(input())

for i in range(n):
  a,b = map(int,input().split())
  ladder[a].append(b)
  ladder[b].append(a)

visited = [False] * const
def dfs(v,max_num):
  visited[v] = True
  for i in ladder[v]:
    if visited[i] == False:
      max_num = max(max_num,i)
      dfs(i,max_num)
  print("v =",v,",max_num =",max_num)
  return max_num

print(dfs(1,1))
