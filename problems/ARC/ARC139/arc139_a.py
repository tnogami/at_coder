N = int(input())
T = list(map(int,input().split()))

upper_bit = -1
lower_bit = 0
val = 0
A = []

for t in T:
    if upper_bit < t:
        val = int("1"+"0"*t, 2)
        upper_bit = t
        lower_bit = t
    elif bit == t:
        tmp = int("1"+"0"*(t+1), 2)
        val |= tmp
    else:
        tmp = int("1"+"0"*t, 2)
        val |= tmp
        bit = t
    A.append(val)

print(A)
print(val)



