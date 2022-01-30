N = int(input())
A = list(map(int,input().split()))
evenA = []
oddA = []

for i, a in enumerate(A):
    if i%2 == 0:
        evenA.append(a)
    else:
        oddA.append(a)

evenS = sum(evenA)
oddS = sum(oddA)

evenA_sorted = sorted(evenA, reverse=True)
oddA_sorted = sorted(oddA, reverse=True)

even_num = -(-N//2)
odd_num = N//2
ans1 = evenS/even_num
tmp_num = even_num
for a in oddA_sorted:
    if a < ans1:
        break
    else:
        ans1 = (ans1*tmp_num+a)/(tmp_num+1)
        tmp_num += 1

ans2 = oddS/odd_num
tmp_num = odd_num
for a in evenA_sorted:
    if a < ans2:
        break
    else:
        ans2 = (ans2*tmp_num+a)/(tmp_num+1)
        tmp_num += 1       
print(max(ans1, ans2))


