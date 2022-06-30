import bisect

N = int(input())
S = input()
W = list(map(int,input().split()))
adults = [10**12]
children = []

for s, w in zip(S,W):
    if s == "0":
        children.append(w)
    else:
        adults.append(w)


adults.sort()
children.sort()

num_adults = len(adults) - 1

ans = 0

for i, w in enumerate(adults):
    tmp = num_adults - i
    idx = bisect.bisect_left(children, w)
    tmp += idx
    ans = max(ans,tmp)

print(ans)