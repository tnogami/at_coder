H, W = map(int, input().split())
S = [input() for _ in range(H)]
snuke = list('snuke')

def check(i, j):
    ret = False
    
    # 右
    if j + 4 < W:
        ans = []
        for k in range(5):
            if S[i][j+k] != snuke[k]:
                break
            ans.append((i+1, j+1+k))
        else:
            ret = True
            return ret, ans

    # 左
    if 0 <= j - 4:
        ans = []
        for k in range(5):
            if S[i][j-k] != snuke[k]:
                break
            ans.append((i+1, j+1-k))
        else:
            ret = True
            return ret, ans

    # 下
    if i + 4 < H:
        ans = []
        for k in range(5):
            if S[i+k][j] != snuke[k]:
                break
            ans.append((i+1+k, j+1))
        else:
            ret = True
            return ret, ans


    # 上
    if 0 <= i - 4:
        ans = []
        for k in range(5):
            if S[i-k][j] != snuke[k]:
                break
            ans.append((i+1-k, j+1))
        else:
            ret = True
            return ret, ans

    # 左上
    if 0 <= i - 4 and 0 <= j-4:
        ans = []
        for k in range(5):
            if S[i-k][j-k] != snuke[k]:
                break
            ans.append((i+1-k, j+1-k))
        else:
            ret = True
            return ret, ans

    # 左下
    if i + 4 < H and 0 <= j - 4:
        ans = []
        for k in range(5):
            if S[i+k][j-k] != snuke[k]:
                break
            ans.append((i+1+k, j+1-k))
        else:
            ret = True
            return ret, ans        

    # 右上
    if j + 4 < W and 0 <= i - 4:
        ans = []
        for k in range(5):
            if S[i-k][j+k] != snuke[k]:
                break
            ans.append((i+1-k, j+1+k))
        else:
            ret = True
            return ret, ans        

    # 右下
    if j + 4 < W and i + 4 < H:
        ans = []
        for k in range(5):
            if S[i+k][j+k] != snuke[k]:
                break
            ans.append((i+1+k, j+1+k))
        else:
            ret = True
            return ret, ans        


    return ret, []

for i in range(H):
    for j in range(W):
        ret, ans = check(i,j)
        if ret:
            for a in ans:
                print(*a)
