def check(i,j):
    ct = 0
    for k in range(6):
        if N<=j+k:break
        if field[i][j+k] == "#": ct+=1
        if k == 5 and 4 <= ct : return True

    ct = 0
    for k in range(6):
        if N<=i+k:break
        if field[i+k][j] == "#": ct+=1
        if k == 5 and 4 <= ct : return True

    ct = 0
    for k in range(6):
        if N<=j+k or N<=i+k:break
        if field[i+k][j+k] == "#": ct+=1
        if k == 5 and 4 <= ct : return True

    ct = 0
    for k in range(6):
        if N<=i+k or N<=j-k or j-k<0:break
        if field[i+k][j-k] == "#": ct+=1
        if k == 5 and 4 <= ct : return True
    
    return False

N = int(input())
field = [input() for _ in range(N)]

ans = False
for i in range(N):
    for j in range(N):
        ans = ans or check(i,j)

if ans:
    print("Yes")
else:
    print("No")




