
string = " abcdefghijklmnopqrstuvwxyz"

P = list(map(int,input().split()))

ans = ""

for p in P:
    ans += string[p]

print(ans)