from collections import Counter 

# def make_divisors(n):
#     lower_divisors , upper_divisors = [], []
#     i = 1
#     while i*i <= n:
#         if n % i == 0:
#             lower_divisors.append(i)
#             if i != n // i:
#                 upper_divisors.append(n//i)
#         i += 1
#     return lower_divisors + upper_divisors[::-1]


N = int(input())
A = list(map(int,input().split()))
ct = Counter(A)
ans = 0
# for a in A:
#     for t in make_divisors(a):
#         ans += ct[a//t]*ct[t]
maxA = max(A)
for i in range(1, maxA+1):
    for j in range(1, maxA+1):
        if maxA < i*j : break
        ans += ct[i]*ct[j]*ct[i*j]

print(ans)
