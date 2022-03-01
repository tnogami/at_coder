N = int(input())
R = list(map(int,input().split()))
C = list(map(int,input().split()))

q = int(input())

ans = []
for _ in range(q):
    r, c = map(int, input().split())
    if R[r-1] + C[c-1] <= N:
        ans.append(".")
    else:
        ans.append("#")
print("".join(ans))

    
