N = int(input())
T = list(map(int,input().split()))

A = []
a = 0

for t in T:
    b = 2**t
    if a < b:
        A.append(b)
        a = b
    else:
        for i in range(t):
            a = a >> 1
        for i in range(t):
            a = a << 1
        tmp = a + b
        if bin(tmp)[-(t+1)] == "1":
            A.append(tmp)
            a = tmp
        else:
            A.append(tmp+b)        
            a = tmp+b
print(A[-1])
