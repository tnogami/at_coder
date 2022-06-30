from collections import deque

def f(s):

    nodes = [[] for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if i == j : continue
            from_x, from_y, from_p = XYP[i]
            to_x, to_y, to_p = XYP[j]
            if abs(from_x - to_x) + abs(from_y - to_y) <= s*from_p :
                nodes[i].append(j)

    for n in range(N):

        dq = deque([n])
        visited = [False] * N
        visited[n] = True

        while dq:
            cur = dq.popleft()
            
            for to in nodes[cur]:
                if visited[to] : continue
                dq.append(to)
                visited[to] = True

        if all(visited) : return True
    
    return False
        
N = int(input())
XYP = [tuple(map(int,input().split())) for _ in range(N)]

ans = 10**10

ng = 0
ok = 10**10
while 1 < abs(ng-ok):
    mid = (ok+ng)//2
    if f(mid):
        ok = mid
    else:
        ng = mid

print(ok)
