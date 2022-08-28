N = int(input())
ans = 3.5
while N != 1:
    ans = max(1, ans)/6 + max(2, ans)/6 + max(3, ans)/6 + max(4, ans)/6 + max(5, ans)/6 + max(6, ans)/6
    N -= 1
print(ans)
