def count(cost:list)->int:
    for k in range(N):
        for i in range(N):
            for j in range(N):
                cost[i][j] = min(cost[i][j], cost[i][k] + cost[k][j]) 
    ct = 0    
    for i,a in enumerate(cost):
        for j in range(i+1,N):
            if a[j] <= P : ct += 1
    return ct

def trans(A:list, X:int)->list:
    ret = []
    for a in A:
        tmp = []
        for i in a:
            if i == -1 :
                tmp.append(X)
            else:
                tmp.append(i)
        ret.append(tmp)
    return ret


N, P, K = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]

#上限を試す
cost = trans(A, 10**10)
c_inf = count(cost)
                
#下限を試す
cost = trans(A, 1)             
c_zero = count(cost)

if c_inf == K:
    print("Infinity")
    exit()
elif K < c_inf or c_zero < K:
    print(0)
    exit()

#上界を探索
ok = 1
ng = 10**10
while 1 < abs(ng-ok):
    m = (ok+ng)//2
    cost = trans(A, m)
    ct = count(cost)
    if ct < K:
        ng = m
    else:
        ok = m
upper = ok

#下界を探索
ok = 10**10
ng = 0
while 1 < ok-ng:
    m = (ok+ng)//2
    cost = trans(A, m)
    ct = count(cost)
    if K < ct:
        ng = m
    else:
        ok = m

lower = ok

print(upper-lower+1)