N = int(input())
A = input().split()
digit = []
ans = N*(N-1)//2
for i in range(len(A)-1):
    for j in range(i+1, len(A)):
        a = A[i].zfill(7)
        b = A[j].zfill(7)
        for k in range(7):
            if 9 < int(a[k]) + int(b[k]):
                ans -= 1
                break

print(ans)