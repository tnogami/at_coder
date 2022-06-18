h1, h2, h3, w1, w2, w3 = map(int, input().split())
ans = 0
for l1 in range(1,h1-1):
    for l2 in range(1, h1-l1):
        l3 = h1 - l1 - l2
        for m1 in range(1,h2-1):
            for m2 in range(1, h2-m1):
                m3 = h2 - m1 - m2
                for n1 in range(1,h3-1):
                    for n2 in range(1, h3-n1):
                        n3 = h3 - n1 - n2

                        if w1 == l1+m1+n1 and w2 == l2+m2+n2 and w3 == l3+m3+n3:ans += 1

print(ans)