import collections

N, M = map(int, input().split())

q = []

ontop = [[] for i in range(N+1)]
stack = collections.deque()

for i in range(M):
    k = int(input())
    a = collections.deque(list(map(int, input().split())))
    q.append(a)
    color = a[0]
    ontop[color].append(i)
    if len(ontop[color]) == 2:
        stack.append(color)

count = 0

while len(stack) != 0:
    color = stack.popleft()
    x, y = ontop[color]
    count += 1
    q[x].popleft()
    if len(q[x]) != 0:
        new_color = q[x][0]
        ontop[new_color].append(x)
        if len(ontop[new_color]) == 2:
            stack.append(new_color)
    q[y].popleft()
    if len(q[y]) != 0:
        new_color = q[y][0]
        ontop[new_color].append(y)
        if len(ontop[new_color]) == 2:
            stack.append(new_color)
    
if count == N:
    print("Yes")
else:
    print("No")
    






