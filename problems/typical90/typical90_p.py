N = int(input())
a,b,c = list(map(int, input().split()))

ans = 9999999
for i in range(10000):
    for j in range(10000):
        if 9999 < i+j : break
        if N < i*a+j*b : break
        if (N-i*a-j*b)%c == 0 :
            k = (N-i*a-j*b)//c
            ans = min(ans, i+j+k)

print(ans)