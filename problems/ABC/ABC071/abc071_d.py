N = int(input())
S1 = input()
S2 = input()

L = ""

for i in range(N):
    if S1[i] == S2[i]:
        L += "A"
    else:
        L += "B"
L = L.replace("BB", "B")

#AB *2
#AA *2
#BA *1
#BB *3
if L[0] == "A":
    ans = 3
else:
    ans = 6

for i in range(len(L)-1):
    s = L[i:i+2]
    if s == "AA":
        ans *= 2
    elif s == "AB":
        ans *= 2
    elif s == "BA":
        ans *= 1
    else:
        ans *= 3
    ans%=1000000007
print(ans)

    