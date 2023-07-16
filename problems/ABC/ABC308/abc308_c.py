from functools import cmp_to_key


def cmp(a, b):  # a = [x_a, y_a], b = [x_b / y_b]
    # 比較対象の分数 a と b が等しければ 0 を返す
    if a[0] * b[1] == b[0] * a[1]:
        return 0
    # a, bという順で並んでほしい条件のときは-1を返し、それ以外では1を返す
    return -1 if a[0] * b[1] < b[0] * a[1] else 1


N = int(input())

l = 1
AB = []
for i in range(N):
    a, b = map(int, input().split())
    AB.append((a, a+b, i+1))

ans = sorted(AB, key=cmp_to_key(cmp), reverse=True)

ans = map(lambda x: x[2], ans)
print(*ans)
