from heapq import heappop, heappush, heapify

N, K = map(int, input().split())
A = list(map(int,input().split()))

A.sort()
hq = [0]

ans = set()
made = set()

while len(ans) <= K:
    num = heappop(hq)
    ans.add(num)
    for a in A:
        if num + a not in made:
            heappush(hq, num+a)
            made.add(num+a)
            
ans = list(ans)
ans.sort()
print(ans[K])