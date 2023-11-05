NandT = input().split()
N = int(NandT[0])
T = NandT[1]

ans = []
for n in range(1, N+1):
    S = input()
    if S == T:
        ans.append(n)
    elif len(S) == len(T):
        error_ct = 0
        for i in range(len(S)):
            if S[i] != T[i]:
                error_ct += 1
        if error_ct == 1:
            ans.append(n)
    elif len(S) == len(T)+1:  # 文字が削除された場合
        error_ct = 0
        for i in range(len(S)):
            if error_ct > 1:
                break

            if error_ct == 1:
                if S[i] != T[i-1]:
                    error_ct += 1
            else:
                if i == len(S)-1:
                    break
                if S[i] != T[i]:
                    error_ct += 1

        if error_ct < 2:
            ans.append(n)

    elif len(S) == len(T)-1:  # 文字が追加された場合
        error_ct = 0
        for i in range(len(T)):
            if error_ct > 1:
                break
            if error_ct == 1:
                if S[i-1] != T[i]:
                    error_ct += 1
            else:
                if i == len(T)-1:
                    break
                if S[i] != T[i]:
                    error_ct += 1

        if error_ct < 2:
            ans.append(n)

print(len(ans))
print(*ans)
