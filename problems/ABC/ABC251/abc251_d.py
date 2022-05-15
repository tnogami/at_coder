W = int(input())
ans = []
for i in range(1,100):
    ans.append(i)
    ans.append(i*10**2)
    ans.append(i*10**4)

print(len(ans))
print(*ans)





