import copy
import queue

M = int(input())
nodes = [[] for i in range(9)]
for i in range(M):
    u, v = map(int, input().split())
    nodes[u-1].append(v-1)
    nodes[v-1].append(u-1)

que = queue.Queue()
pieces = list(map(int, input().split()))
st = 45 - sum(pieces) - 1
pattern = set([])

que.put([st,0,pieces])
pattern.add("".join(list(map(str, pieces))))
ans = -1
 
#キューが無くなるまでループ
while not que.empty():
    n, ct, p = que.get()
    if p == [1, 2, 3, 4, 5, 6, 7, 8]:
        ans = ct
        break
 
    for to in nodes[n]:
        new_p = copy.copy(p)
        new_p[p.index(to+1)] = n + 1 #駒の移動
        new_pattern = "".join(list(map(str, new_p)))
        if new_pattern in pattern : continue
        que.put([to, ct+1, new_p])
        pattern.add(new_pattern)

print(ans)