from itertools import accumulate
N, W = map(int, input().split())
STP = [tuple(map(int,input().split())) for _ in range(N)]
time_range = max(STP, key=lambda x:x[1])[1]

water_comsuption = [0]*(time_range+10)

for s,t,p in STP:
    water_comsuption[s] += p
    water_comsuption[t] -= p

water_comsuption = list(accumulate(water_comsuption))

if max(water_comsuption) <= W:
    print("Yes")
else:
    print("No")