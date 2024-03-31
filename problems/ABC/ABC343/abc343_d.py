N, T = map(int, input().split())

points = [0]*N
d_point = {0:N}

for _ in range(T):
    a, b = map(int,input().split())
    a -= 1
    cur_point = points[a]
    points[a] += b
    d_point[cur_point] -= 1
    if d_point[cur_point] == 0:
        del d_point[cur_point]
    
    new_point = cur_point + b
    if new_point in d_point:
        d_point[new_point] += 1
    else:
        d_point[new_point] = 1

    print(len(d_point))
