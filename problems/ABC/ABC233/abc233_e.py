X = [int(x) for x in input()]
s = sum(X)
ans = [str(s%10)]
kuriagari = s//10
for x in X[::-1]:
    s -= x
    tmp = kuriagari + s
    if tmp == 0 : break
    if 9 < tmp:
        ans.append(str(tmp%10))
        kuriagari = tmp//10
    else:
        ans.append(str(tmp%10))
        kuriagari = 0
print("".join(ans[::-1]))
