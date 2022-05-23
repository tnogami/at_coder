def dfs(x,y,z)->int:
    if x == 100 or y == 100 or z == 100:
        d[(x,y,z)] = 0
        return 0

    if (x,y,z) in d:
        return d[(x,y,z)]

    m = x+y+z
    ret = 0
    ret += (x/m)*(dfs(x+1,y,z)+1)
    ret += (y/m)*(dfs(x,y+1,z)+1)
    ret += (z/m)*(dfs(x,y,z+1)+1)
    d[(x,y,z)] = ret
    return ret


from collections import defaultdict
A, B, C = map(int, input().split())

d = defaultdict(int)

print(dfs(A,B,C))


