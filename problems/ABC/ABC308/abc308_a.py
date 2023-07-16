A = list(map(int, input().split()))

flag = True
for a in A:
    if a < 100 or 675 < a:
        flag = False

    if a % 25 != 0:
        flag = False

for i in range(len(A)-1):
    if A[i] > A[i+1]:
        flag = False

if flag:
    print("Yes")
else:
    print("No")
