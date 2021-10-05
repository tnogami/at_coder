N = int(input())
for ans in range(0,61):
    if N < 2**ans : break
print(ans-1)
