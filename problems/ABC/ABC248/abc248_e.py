from itertools import combinations
from collections import defaultdict
from fractions import Fraction

def main():
    N, K = map(int, input().split())
    XY = [tuple(map(int, input().split())) for _ in range(N)]
    if K == 1:
        print("Infinity")
        return

    d = defaultdict(int)
    for i,j in combinations(range(N), 2):
        x1, y1 = XY[i]
        x2, y2 = XY[j]

        if x1 == x2:
            d[("inf", x1)] += 1
        elif y1 == y2:
            d[(0, y1)] += 1
        else:
            a = Fraction((y2-y1),(x2-x1))
            b = y1-a*x1
            d[(str(a),str(b))] += 1

    req_k = K*(K-1)//2
    ans = 0
    for k in d.values():
        if req_k <= k: ans+=1
    print(ans)

if __name__ == "__main__":
    main()
    