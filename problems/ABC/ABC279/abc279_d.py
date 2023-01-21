import math

def calc_div(k):
    t = B - 0.5*A/((1+k)*math.sqrt(1+k))
    return t

def calc_time(k):
    t = k*B + A/(math.sqrt(1+k))
    return t

A, B = map(int, input().split())

k_min = 0

for i in range(100):
    k = 10**i
    t = k*B + A/(math.sqrt(1+k))
    if A < t: break

k_max = k

while 1 < abs(k_min - k_max):
    k_mid = (k_max+k_min)//2
    t_max = calc_div(k_max)
    t_min = calc_div(k_min)
    t_mid = calc_div(k_mid)

    if 0 < t_mid:
        k_max = k_mid
    else:
        k_min = k_mid

print(min(calc_time(k_max), calc_time(k_min)))