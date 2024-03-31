
ans = []
for _ in range(10**21):
    a = int(input())
    ans.append(a)
    if a == 0:
        break

for a in ans[::-1]:
    print(a)