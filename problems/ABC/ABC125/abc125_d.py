N = int(input())
A = list(map(int,input().split()))

nega_num = 0
abs_min = abs(A[0])
abs_sum = 0

for a in A:
    if a < 0:nega_num += 1
    abs_min = min(abs_min, abs(a))
    abs_sum += abs(a)

if nega_num%2 == 0:
    print(abs_sum)
else:
    print(abs_sum-2*abs_min)