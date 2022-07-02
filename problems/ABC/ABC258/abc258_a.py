K = int(input())
if 60 <= K:
    h = "22"
    m = str(K-60).zfill(2)
else:
    h = "21"
    m = str(K).zfill(2)
print(h+":"+m)

