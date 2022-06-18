H, W = map(int, input().split())
field = [input() for _ in range(H)]
l = []
for i in range(H):
    for j in range(W):
        if field[i][j] == "o":l.append((i,j))
print( abs(l[0][0]-l[1][0])+abs(l[0][1]-l[1][1]) )

