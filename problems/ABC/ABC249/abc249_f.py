from heapq import heappush, heappop
N, K = map(int, input().split())
query = [tuple(map(int, input().split())) for _ in range(N)]
query = query[::-1]
query.append((1,0))

plus_sum = 0
minus_ct = 0
minus_list = []
ans = -10**18
for t, y in query:
    if t == 1:
        ans = max(ans, y + plus_sum)
        K -= 1
        if K < minus_ct:
            if not minus_list:break
            tmp = heappop(minus_list)
            plus_sum -= tmp             
    else:
        if 0 <= y:
            plus_sum += y
        else:
            minus_ct += 1
            if K < minus_ct:
                heappush(minus_list, -y)
                tmp = heappop(minus_list)
                plus_sum -= tmp
            else:
                heappush(minus_list, -y)
                
    if K < 0 : break

print(ans)


