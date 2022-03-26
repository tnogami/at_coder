S = input().split()
T = input().split()

inv_s = 0
for i in [0,1]:
    for j in range(i+1,3):
        if S[i] > S[j] :
            inv_s += 1

inv_t = 0
for i in [0,1]:
    for j in range(i+1,3):
        if T[i] > T[j] : inv_t += 1

if inv_t%2 == inv_s%2:
    print("Yes")
else:
    print("No")