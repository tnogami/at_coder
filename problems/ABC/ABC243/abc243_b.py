N = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))

ans1 = 0
for i in range(N):
    if A[i]==B[i]: ans1+=1


ans2 = 0
B = set(B)

for a in A:
    if a in B: ans2+=1

print(ans1)
print(ans2-ans1)

